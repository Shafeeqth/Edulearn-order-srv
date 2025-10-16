import asyncio
import json
from aiokafka import AIOKafkaConsumer
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from uuid import uuid4


from src.application.interfaces.logging_interface import ILoggingService
from src.application.interfaces.kafka_producer_interface import IKafkaProducer
from src.domain.exceptions.exceptions import OrderNotFoundException
from src.domain.repositories.order_repository import IOrderRepository
from src.domain.repositories.session_booking_repository import ISessionBookingRepository
from src.infrastructure.config.settings import settings
from src.shared.events.topics import EVENT_TOPICS

# Import Use Cases
from src.application.use_cases.order.order_payment_initiated_use_case import OrderPaymentInitiatedUseCase
from src.application.use_cases.order.order_success_use_case import OrderSuccessUseCase
from src.application.use_cases.order.order_failed_use_case import OrderFailedUseCase

from src.application.dtos.order_payment_initiate_dto import OrderPaymentInitiatedDto
from src.application.dtos.order_payment_failure_dto import OrderPaymentFailureDto
from src.application.dtos.order_success_dto import OrderPaymentSuccessDto


class KafkaConsumer:
    def __init__(
        self,
        order_repository: IOrderRepository,
        session_booking_repository: ISessionBookingRepository,
        payment_initiated_usecase: OrderPaymentInitiatedUseCase,
        order_success_usecase:  OrderSuccessUseCase,
        order_failed_usecase: OrderFailedUseCase,
        kafka_producer: IKafkaProducer,
        redis,
        metrics_service,
        logging_service: ILoggingService,
    ):

        payment_topics = [
            EVENT_TOPICS.PAYMENT_ORDER_INITIATED.value,
            EVENT_TOPICS.PAYMENT_ORDER_SUCCEEDED.value,
            EVENT_TOPICS.PAYMENT_ORDER_FAILED.value,
        ]

        self.consumer = AIOKafkaConsumer(
            *payment_topics,
            bootstrap_servers=settings.KAFKA_BROKER,
            group_id=settings.KAFKA_CONSUMER_GROUP or "order-service-group",
            auto_offset_reset="latest",
            enable_auto_commit=False,
            max_poll_records=settings.KAFKA_CONSUMER_MAX_POLL_RECORDS,
        )

        self.order_repository = order_repository
        self.payment_initiated_usecase = payment_initiated_usecase
        self.order_success_usecase = order_success_usecase
        self.order_failed_usecase = order_failed_usecase
        self.session_booking_repository = session_booking_repository
        self.kafka_producer = kafka_producer
        self.redis = redis
        self.metrics_service = metrics_service
        self.logger = logging_service.get_logger("KafkaConsumer")

        # Dead-letter queue
        self.dlq_topic = "order-service.events.dlq"

        # # Initialize use cases
        # self.payment_initiated_usecase = OrderPaymentInitiatedUseCase(
        #     order_repository, kafka_producer, redis, logging_service, metrics_service
        # )
        # self.order_success_usecase = OrderSuccessUseCase(
        #     order_repository, kafka_producer, redis, logging_service, metrics_service
        # )
        # self.order_failed_usecase = OrderFailedUseCase(
        #     order_repository, kafka_producer, redis, logging_service, metrics_service
        # )

        self.executor = ThreadPoolExecutor(max_workers=10)

    async def start(self):
        await self.consumer.start()
        self.logger.info(
            "✅ Kafka Consumer started and listening for order events...")
        try:
            async for msg in self.consumer:
                await self.handle_message(msg)
                await self.consumer.commit()
        except Exception as e:
            self.logger.error(f"❌ Consumer crashed: {str(e)}")
        finally:
            await self.consumer.stop()
            self.executor.shutdown()

    async def handle_message(self, msg):
        """Handle a single Kafka message"""
        try:
            payload = json.loads(msg.value.decode("utf-8"))
            topic = msg.topic

            self.logger.info(f"📥 Received event from topic: {topic}")
            await self.route_event(topic, payload)

        except json.JSONDecodeError:
            self.logger.error(
                f"Invalid JSON in message from topic {msg.topic}")
            await self.send_to_dlq(msg, error="JSONDecodeError")
        except Exception as e:
            self.logger.error(f"Error processing message: {str(e)}")
            await self.send_to_dlq(msg, error=str(e))

    async def route_event(self, topic: str, payload: dict):
        """Route events to corresponding use cases"""
        try:
            if topic == EVENT_TOPICS.PAYMENT_ORDER_INITIATED.value:
                # Use named arguments when instantiating a Pydantic model from a dict
                dto = OrderPaymentInitiatedDto(
                    created_at=payload["createdAt"],
                    order_id=payload["orderId"],
                    provider=payload["provider"],
                    payment_id=payload["paymentId"],
                    provider_order_id=payload["providerOrderId"],
                    payment_status=payload["paymentStatus"],
                )
                await self.payment_initiated_usecase.execute(dto)

            elif topic == EVENT_TOPICS.PAYMENT_ORDER_SUCCEEDED.value:
                dto = OrderPaymentSuccessDto(
                    created_at=payload["createdAt"],
                    order_id=payload["orderId"],
                    provider=payload["provider"],
                    payment_status=payload["paymentSatus"],
                    payment_id=payload["paymentId"],
                    provider_order_id=payload["providerOrderId"],
                )
                await self.order_success_usecase.execute(dto)

            elif topic == EVENT_TOPICS.PAYMENT_ORDER_FAILED.value:
                dto = OrderPaymentFailureDto(
                    created_at=payload["createdAt"],
                    order_id=payload["orderId"],
                    provider=payload["provider"],
                    payment_status=payload["paymentSatus"],
                    payment_id=payload["paymentId"],
                    provider_order_id=payload["providerOrderId"],
                )
                await self.order_failed_usecase.execute(dto)

            else:
                self.logger.warning(f"⚠️ Unknown topic received: {topic}")

        except OrderNotFoundException as e:
            self.logger.error(f"Order not found: {str(e)}")
            await self.send_to_dlq_from_payload(topic, payload, error=str(e))
        except Exception as e:
            self.logger.error(f"Failed to process event for {topic}: {str(e)}")
            await self.send_to_dlq_from_payload(topic, payload, error=str(e))

    async def send_to_dlq(self, msg, error: str):
        """Send failed message to DLQ"""
        dlq_event = {
            "eventType": "DLQEvent",
            "originalTopic": msg.topic,
            "originalMessage": msg.value.decode("utf-8", errors="ignore"),
            "error": error,
            "timestamp": datetime.utcnow().isoformat(),
        }
        await self.kafka_producer.publish_event(self.dlq_topic, event=dlq_event, schema=None)
        self.logger.warning(f"🚨 Sent message to DLQ topic {self.dlq_topic}")

    async def send_to_dlq_from_payload(self, topic: str, payload: dict, error: str):
        """Send failed payload (non-message object) to DLQ"""
        dlq_event = {
            "eventType": "DLQEvent",
            "originalTopic": topic,
            "originalMessage": json.dumps(payload),
            "error": error,
            "timestamp": datetime.utcnow().isoformat(),
        }
        await self.kafka_producer.publish_event(self.dlq_topic, event=dlq_event, schema=None)
        self.logger.warning(f"🚨 Sent payload to DLQ topic {self.dlq_topic}")
