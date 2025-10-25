from src.application.dtos.order_payment_failure_dto import OrderPaymentFailureDto
from src.domain.entities.payment_details import PaymentDetails, PaymentStatus
from src.shared.events.topics import EVENT_TOPICS
from src.infrastructure.database.database import get_db
from src.domain.exceptions.exceptions import OrderNotFoundException
from tenacity import retry, stop_after_attempt, wait_exponential


class OrderFailedUseCase:
    def __init__(self, order_repository, kafka_producer, redis, logging_service, metrics_service):
        self.order_repository = order_repository
        self.kafka_producer = kafka_producer
        self.redis = redis
        self.logger = logging_service.get_logger("OrderFailedUseCase")
        self.metrics = metrics_service

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def execute(self, dto: OrderPaymentFailureDto):
        self.logger.info(f"Processing failed payment for order {dto.order_id}")

        async with get_db() as session:
            order = await self.order_repository.find_by_id(dto.order_id, session)
            if not order:
                raise OrderNotFoundException(
                    f"Order not found: {dto.order_id}")

            if not order.payment_details:
                payment_details = PaymentDetails(
                    payment_id=dto.payment_id,
                    provider=dto.provider,
                    provider_order_id=dto.provider_order_id,
                    payment_status="pending",
                )
                order.set_payment_details(payment_details)
            else:
                order.payment_details.setStatus("pending")

            order.mark_failed()
            await self.order_repository.save(order, session)

        await self.kafka_producer.publish_event(
            EVENT_TOPICS.ORDER_COURSE_FAILED.value,
            event={
                "orderId": order.id,
                "userId": order.user_id,
                "items": [{"course_id": i.course_id, "price": i.price} for i in order.items],
                "amount": order.amount.amount,
                "currency": order.amount.currency,
            },
            schema=None,
        )

        self.logger.warning(f"❌ Order {dto.order_id} marked as FAILED")
        return
