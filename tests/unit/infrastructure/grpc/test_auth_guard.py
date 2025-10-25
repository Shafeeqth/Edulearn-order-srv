import pytest
from unittest.mock import AsyncMock
import logging

from src.infrastructure.grpc.auth_guard import AuthGuard

@pytest.mark.asyncio
async def test_auth_guard_success(user_service_client):
    # Arrange
    logger = logging.getLogger("test")
    auth_guard = AuthGuard(user_service_client, logger)
    token = "valid_token"

    # Act
    user_info = await auth_guard.validate_token(token)

    # Assert
    assert user_info == {"user_id": "user1", "role": "STUDENT"}
    user_service_client.verify_user.assert_called_once_with("user1", token)

@pytest.mark.asyncio
async def test_auth_guard_authorize_failure(user_service_client):
    # Arrange
    logger = logging.getLogger("test")
    auth_guard = AuthGuard(user_service_client, logger)
    user_service_client.verify_user.return_value = {"user_id": "user1", "role": "INSTRUCTOR"}
    token = "valid_token"

    # Act & Assert
    user_info = await auth_guard.validate_token(token)
    with pytest.raises(ValueError, match="User role INSTRUCTOR not authorized for this action"):
        await auth_guard.authorize(user_info, required_role="STUDENT")