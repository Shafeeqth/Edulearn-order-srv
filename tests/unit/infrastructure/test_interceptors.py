import pytest
import grpc
from unittest.mock import AsyncMock
from order.src.infrastructure.grpc.interceptors.client_inerceptors import ClientAuthInterceptor
from src.infrastructure.grpc.interceptors.server_interceptor import (
    ServerLoggingInterceptor,
    ServerMetricsInterceptor,
    ServerTracingInterceptor,
    ServerAuthInterceptor,
)
import logging

@pytest.mark.asyncio
async def test_server_logging_interceptor():
    # Arrange
    logger = logging.getLogger("test")
    logger.info = AsyncMock()
    interceptor = ServerLoggingInterceptor(logger)
    continuation = AsyncMock(return_value="response")
    handler_call_details = grpc.HandlerCallDetails(method="/order_service.OrderService/PlaceOrder", invocation_metadata={})

    # Act
    response = await interceptor.intercept_service(continuation, handler_call_details)

    # Assert
    assert response == "response"
    logger.info.assert_called_once_with("Received gRPC request: /order_service.OrderService/PlaceOrder")

@pytest.mark.asyncio
async def test_server_metrics_interceptor():
    # Arrange
    interceptor = ServerMetricsInterceptor(logging.getLogger("test_logger"))
    continuation = AsyncMock(return_value="response")
    handler_call_details = grpc.HandlerCallDetails(method="/order_service.OrderService/PlaceOrder", invocation_metadata={})

    # Act
    response = await interceptor.intercept_service(continuation, handler_call_details)

    # Assert
    assert response == "response"

@pytest.mark.asyncio
async def test_server_auth_interceptor():
    # Arrange
    logger = logging.getLogger("test")
    auth_guard = AsyncMock()
    auth_guard.validate_token.return_value = {"user_id": "user1", "role": "STUDENT"}
    auth_guard.authorize.return_value = None
    interceptor = ServerAuthInterceptor(auth_guard, logger)
    continuation = AsyncMock(return_value="response")
    handler_call_details = grpc.HandlerCallDetails(
        method="/order_service.OrderService/PlaceOrder",
        invocation_metadata=[("authorization", "Bearer token")]
    )

    # Act
    response = await interceptor.intercept_service(continuation, handler_call_details)

    # Assert
    assert response == "response"
    auth_guard.validate_token.assert_called_once_with("token")
    auth_guard.authorize.assert_called_once_with({"user_id": "user1", "role": "STUDENT"}, "STUDENT")

@pytest.mark.asyncio
async def test_client_auth_interceptor():
    # Arrange
    interceptor = ClientAuthInterceptor("test-token")
    continuation = AsyncMock(return_value="response")
    client_call_details = grpc.ClientCallDetails(
        method="/user_service.UserService/VerifyUser",
        metadata={},
        timeout=None,
        credentials=None,
        wait_for_ready=None,
    )
    request = "request"

    # Act
    response = await interceptor.intercept(continuation, client_call_details, request)

    # Assert
    assert response == "response"
    assert client_call_details.metadata["authorization"] == "Bearer test-token"