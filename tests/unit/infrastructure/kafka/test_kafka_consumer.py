import pytest
from src.infrastructure.kafka.consumer import KafkaConsumer
from src.domain.repositories.order_repository import OrderRepository
from src.domain.repositories.session_booking_repository import SessionBookingRepository
from unittest.mock import AsyncMock
import logging

@pytest.mark.asyncio
async def test_kafka_consumer_process_order_updated(kafka_producer):
    # Arrange
    order_repository = AsyncMock(spec=OrderRepository)
    session_booking_repository = AsyncMock(spec=SessionBookingRepository)
    logger = logging.getLogger("test")
    consumer = KafkaConsumer(order_repository, session_booking_repository, kafka_producer, logger)

    event = {"id": "order1", "status": "COMPLETED"}
    order = AsyncMock()
    order.user_id = "user1"
    order.course_ids = ["course1"]
    order_repository.find_by_id.return_value = order

    # Act
    await consumer.process_order_updated(event)

    # Assert
    order.mark_completed.assert_called_once()
    order_repository.save.assert_called_once_with(order)
    kafka_producer.publish_event.assert_called_once()