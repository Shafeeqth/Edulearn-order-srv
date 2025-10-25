import pytest
from src.application.dtos.order_create_dto import OrderCreateDto
from src.application.dtos.session_booking_create_dto import SessionBookingCreateDTO
from src.application.use_cases.session_booking.session_booking_use_case import BookSessionUseCase
from src.infrastructure.database.repositories.sql_order_repository import SqlOrderRepository
from src.infrastructure.database.repositories.sql_session_booking_repository import SqlSessionBookingRepository
from src.application.use_cases.order.place_order_use_case import PlaceOrderUseCase
import logging
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_place_order_integration(db_session, redis_client, kafka_producer, course_service_client):
    # Arrange
    order_repository = SqlOrderRepository(db_session, redis_client, logging.getLogger("test"))
    logger = logging.getLogger("test")
    use_case = PlaceOrderUseCase(order_repository, kafka_producer, course_service_client, redis_client, logger)
    order_dto = OrderCreateDto(user_id="user1", course_ids=["course1"])

    redis_client.get.side_effect = [None]
    redis_client.client.pipeline.return_value.__aenter__.return_value.get.return_value = None
    redis_client.client.pipeline.return_value.__aenter__.return_value.execute.return_value = [None]

    # Act
    result = await use_case.execute(order_dto)

    # Assert
    assert result.user_id == "user1"
    assert result.course_ids == ["course1"]
    assert result.total_amount == 100.0

    # Verify database state
    saved_order = await order_repository.find_by_id(result.id)
    assert saved_order.user_id == "user1"

@pytest.mark.asyncio
async def test_book_session_integration(db_session, redis_client, kafka_producer, session_service_client):
    # Arrange
    session_booking_repository = SqlSessionBookingRepository(db_session, redis_client, logging.getLogger("test"))
    logger = logging.getLogger("test")
    use_case = BookSessionUseCase(session_booking_repository, kafka_producer, session_service_client, redis_client, logger)
    booking_dto = SessionBookingCreateDTO(user_id="user1", session_id="session1")

    redis_client.get.side_effect = [None]
    redis_client.lock.return_value.__aenter__.return_value = AsyncMock()
    session_booking_repository.count_bookings_for_session.return_value = 2

    # Act
    result = await use_case.execute(booking_dto)

    # Assert
    assert result.user_id == "user1"
    assert result.session_id == "session1"
    assert result.amount == 50.0

    # Verify database state
    saved_booking = await session_booking_repository.find_by_id(result.id)
    assert saved_booking.user_id == "user1"
    