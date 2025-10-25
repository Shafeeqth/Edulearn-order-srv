import pytest
from src.application.dtos.session_booking_create_dto import SessionBookingCreateDTO
from src.application.use_cases.session_booking.session_booking_use_case import BookSessionUseCase
from src.domain.repositories.session_booking_repository import SessionBookingRepository
from unittest.mock import AsyncMock
import logging

@pytest.mark.asyncio
async def test_book_session_use_case_success(redis_client, kafka_producer, session_service_client):
    # Arrange
    session_booking_repository = AsyncMock(spec=SessionBookingRepository)
    session_booking_repository.count_bookings_for_session.return_value = 2  # Below max_slots
    logger = logging.getLogger("test")
    use_case = BookSessionUseCase(session_booking_repository, kafka_producer, session_service_client, redis_client, logger)

    redis_client.get.side_effect = [None]  # Cache miss
    redis_client.lock.return_value.__aenter__.return_value = AsyncMock()

    booking_dto = SessionBookingCreateDTO(user_id="user1", session_id="session1")

    # Act
    result = await use_case.execute(booking_dto)

    # Assert
    assert result.user_id == "user1"
    assert result.session_id == "session1"
    assert result.amount == 50.0
    assert result.status == "PENDING"
    assert kafka_producer.publish_event.called
    assert redis_client.client.delete.called_with("session_bookings:session1")

@pytest.mark.asyncio
async def test_book_session_use_case_no_slots(redis_client, kafka_producer, session_service_client):
    # Arrange
    session_booking_repository = AsyncMock(spec=SessionBookingRepository)
    session_booking_repository.count_bookings_for_session.return_value = 10  # Equal to max_slots
    logger = logging.getLogger("test")
    use_case = BookSessionUseCase(session_booking_repository, kafka_producer, session_service_client, redis_client, logger)

    redis_client.get.side_effect = [None]
    redis_client.lock.return_value.__aenter__.return_value = AsyncMock()

    booking_dto = SessionBookingCreateDTO(user_id="user1", session_id="session1")

    # Act & Assert
    with pytest.raises(ValueError, match="Session session1 is fully booked"):
        await use_case.execute(booking_dto)