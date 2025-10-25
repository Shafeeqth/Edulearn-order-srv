import pytest
from src.application.dtos.order_create_dto import OrderCreateDto
from src.application.use_cases.order.place_order_use_case import PlaceOrderUseCase
from src.domain.repositories.order_repository import OrderRepositoryInterface
from unittest.mock import AsyncMock
import logging

@pytest.mark.asyncio
async def test_place_order_use_case_success(redis_client, kafka_producer, course_service_client):
    # Arrange
    order_repository = AsyncMock(spec=OrderRepositoryInterface)
    logger = logging.getLogger("test")
    use_case = PlaceOrderUseCase(order_repository, kafka_producer, course_service_client, redis_client, logger)

    redis_client.get.side_effect = [None]  # Cache miss
    redis_client.client.pipeline.return_value.__aenter__.return_value.get.return_value = None
    redis_client.client.pipeline.return_value.__aenter__.return_value.execute.return_value = [None]

    order_dto = OrderCreateDto(user_id="user1", course_ids=["course1"])

    # Act
    result = await use_case.execute(order_dto)

    # Assert
    assert result.user_id == "user1"
    assert result.course_ids == ["course1"]
    assert result.total_amount == 100.0
    assert result.status == "PENDING"
    assert kafka_producer.publish_event.called
    assert redis_client.client.delete.called_with("user_orders:user1")

@pytest.mark.asyncio
async def test_place_order_use_case_course_not_found(redis_client, kafka_producer, course_service_client):
    # Arrange
    order_repository = AsyncMock(spec=OrderRepositoryInterface)
    logger = logging.getLogger("test")
    use_case = PlaceOrderUseCase(order_repository, kafka_producer, course_service_client, redis_client, logger)

    redis_client.get.side_effect = [None]
    redis_client.client.pipeline.return_value.__aenter__.return_value.get.return_value = None
    redis_client.client.pipeline.return_value.__aenter__.return_value.execute.return_value = [None]
    course_service_client.get_course.side_effect = ValueError("Course not found")

    order_dto = OrderCreateDto(user_id="user1", course_ids=["course1"])

    # Act & Assert
    with pytest.raises(ValueError, match="Course not found"):
        await use_case.execute(order_dto)