import asyncio
from src.shared.events.topics import EVENT_TOPICS
from src.infrastructure.database.database import get_db
from src.domain.entities.order_items import OrderItem
from src.domain.exceptions.exceptions import UserNotFoundException
from src.application.interfaces.logging_interface import ILoggingService
from src.application.interfaces.metrics_interface import IMetricsService
from src.domain.repositories.order_repository import IOrderRepository
from src.application.dtos.order_create_dto import OrderCreateDto
from src.application.dtos.order_dto import OrderDto
from src.application.interfaces.grpc_client_interface import (
    ICourseServiceClient,
    IUserServiceClient,
)
from src.domain.entities.order import Order, OrderStatus
from src.domain.value_objects.money import Money
from src.application.services.saga.saga_orchestrator import SagaOrchestrator
from src.application.services.saga.steps.order_steps import (
    CreateOrderStep,
    RequestPaymentStep,
)
from src.application.interfaces.kafka_producer_interface import IKafkaProducer
from src.application.interfaces.redis_interface import IRedisService
from tenacity import retry, stop_after_attempt, wait_exponential
import json


class PlaceOrderUseCase:
    def __init__(
        self,
        order_repository: IOrderRepository,
        kafka_producer: IKafkaProducer,
        course_service_client: ICourseServiceClient,
        user_service_client: IUserServiceClient,
        redis: IRedisService,
        logging_service: ILoggingService,
        metrics_service: IMetricsService,
    ):
        self.order_repository = order_repository
        self.kafka_producer = kafka_producer
        self.course_service_client = course_service_client
        self.user_service_client = user_service_client
        self.redis = redis
        self.logging_service = logging_service
        self.logger = logging_service.get_logger("PlaceOrderUseCase")
        self.metrics = metrics_service

    async def fetch_course_prices(self, course_ids: list[str]) -> dict[str, float]:
        # Fetch from Redis
        cache_keys = [f"course_price:{course_id}" for course_id in course_ids]
        async with self.redis.client.pipeline() as pipe:
            for key in cache_keys:
                pipe.get(key)
            cached_prices = await pipe.execute()

        uncached_course_ids = []
        prices = {}
        for course_id, cached_price in zip(course_ids, cached_prices):
            if cached_price:
                prices[course_id] = float(cached_price)
                self.metrics.cache_hits(type="course_price")
            else:
                uncached_course_ids.append(course_id)
                self.metrics.cache_misses(type="course_price")

        # Batch fetch uncached courses
        if uncached_course_ids:
            tasks = [
                self.course_service_client.get_course(course_id)
                for course_id in uncached_course_ids
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            async with self.redis.client.pipeline() as pipe:
                for course_id, result in zip(uncached_course_ids, results):
                    if isinstance(result, (Exception, BaseException)):
                        self.logger.error(
                            f"Failed to fetch course {course_id}: {str(result)}"
                        )
                        raise result
                    prices[course_id] = result["price"]
                    pipe.set(f"course_price:{course_id}", str(
                        result["price"]), ex=3600)
                await pipe.execute()

        return prices

    # @retry(
    #     stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10)
    # )
    async def execute(self, order_dto: OrderCreateDto, idempotency_key: str | None) -> OrderDto:
        self.logger.info(
            f"Executing PlaceOrderUseCase for user {order_dto.user_id}")

        if idempotency_key:
            async with get_db() as session:
                order = await self.order_repository.find_by_idempotency_key(idempotency_key=idempotency_key, session=session)
                if order:
                    self.logger.info(
                        f"Order exist with idempotency_key {idempotency_key} skipping creation")
                    return OrderDto.from_domain(order)

        # Batch fetch course prices
        user = await self.user_service_client.get_user(order_dto.user_id)
        if not user:
            raise UserNotFoundException(
                f"User not found with Id {order_dto.user_id}")

        prices = await self.fetch_course_prices(order_dto.course_ids)

        # Convert all price values to its as integers representing the smallest currency unit
        prices_in_scu = {course_id: price *
                         100 for course_id, price in prices.items()}

        total_amount = sum(prices_in_scu[course_id]
                           for course_id in order_dto.course_ids)

        order_items = [OrderItem(course_id=course_id, price=price)
                       for course_id, price in prices_in_scu.items()]

        # For now, discount is 0 (can be enhanced later)
        discount = 0

        # Subtotal is total_price minus discount (ensure non-negative)
        sub_total = max(total_amount - discount, 0)

        # Create order
        order = Order.create(
            user_id=order_dto.user_id,
            idempotency_key=idempotency_key,
            items=order_items,
            sub_total=sub_total,
            amount=Money(amount=total_amount),
            status=OrderStatus.CREATED,
            discount=discount,
            payment_details=None
        )
        async with get_db() as session:
            await self.order_repository.save(order, session)

        self.logger.debug(
            f"Order creation request has been successful")

        # Publish order created event
        await self.kafka_producer.publish_event(EVENT_TOPICS.ORDER_COURSE_CREATED.value, event={
            "orderId": order.id,
            "userId": order.user_id,
            "idempotencyKey": order.idempotency_key,
            "items": [
                {"course_id": i.course_id, "price": i.price}
                for i in order.items
            ],
            "amount": order.amount.amount,
            "currency": order.amount.currency}, schema=None)

        return OrderDto.from_domain(order)
