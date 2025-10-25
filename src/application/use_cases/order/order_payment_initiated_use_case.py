from src.application.dtos.order_payment_initiate_dto import OrderPaymentInitiatedDto
from src.application.interfaces.kafka_producer_interface import IKafkaProducer
from src.application.interfaces.logging_interface import ILoggingService
from src.application.interfaces.metrics_interface import IMetricsService
from src.application.interfaces.redis_interface import IRedisService
from src.domain.entities.payment_details import PaymentDetails, PaymentStatus
from src.domain.repositories.order_repository import IOrderRepository
from src.infrastructure.database.database import get_db
from src.domain.exceptions.exceptions import OrderNotFoundException
from tenacity import retry, stop_after_attempt, wait_exponential


class OrderPaymentInitiatedUseCase:
    def __init__(self, order_repository: IOrderRepository,
                 kafka_producer: IKafkaProducer,
                 redis: IRedisService,
                 logging_service: ILoggingService,
                 metrics_service: IMetricsService,
                 ):
        self.order_repository = order_repository
        self.kafka_producer = kafka_producer
        self.redis = redis
        self.logger = logging_service.get_logger(
            "OrderPaymentInitiatedUseCase")
        self.metrics = metrics_service

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def execute(self, dto: OrderPaymentInitiatedDto):
        self.logger.info(f"Initiating payment for order {dto.order_id}")

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

            await self.order_repository.save(order, session)

        self.logger.debug(f"✅ Payment initiated for order {dto.order_id}")
        return
