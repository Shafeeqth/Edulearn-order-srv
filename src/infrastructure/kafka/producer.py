import json
import os
from aiokafka import AIOKafkaProducer
import fastavro
import io
import logging
from fastavro.types import Schema
from tenacity import retry, stop_after_attempt, wait_exponential
from src.application.interfaces.logging_interface import ILoggingService
from src.application.interfaces.kafka_producer_interface import (
    IKafkaProducer,
)
from src.infrastructure.config.settings import settings


class KafkaProducer(IKafkaProducer):
    def __init__(self, logger_service: ILoggingService):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BROKER,
            enable_idempotence=True,
            acks="all",
            compression_type="gzip",  # Optimize network usage
        )
        self.logger = logger_service.get_logger("KafkaProducer")

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    async def start(self) -> None:
        try:
            await self.producer.start()
            self.logger.info("Kafka producer started successfully")
        except Exception as e:
            self.logger.error(f"Failed to start Kafka producer: {str(e)}")
            raise

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    async def stop(self) -> None:
        try:
            await self.producer.stop()
            self.logger.info("Kafka producer stopped successfully")
        except Exception as e:
            self.logger.error(f"Failed to stop Kafka producer: {str(e)}")
            raise

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    async def publish_event(self, topic: str, event: dict, schema: Schema | None = None):
        try:
            if schema:
                # Serialize with Avro schema
                bytes_writer = io.BytesIO()
                fastavro.schemaless_writer(bytes_writer, schema, event)
                data = bytes_writer.getvalue()
            else:
                # Serialize as JSON, encode to bytes
                data = json.dumps(event).encode("utf-8")
            await self.producer.send_and_wait(
                topic,
                key=event["orderId"].encode("utf-8"),
                value=data
            )
            self.logger.debug(f"Published event {event.get('eventType', 'unknown')} to topic {topic}")
        except Exception as e:
            self.logger.error(f"Failed to publish event to topic {topic}: {str(e)}")
            raise
