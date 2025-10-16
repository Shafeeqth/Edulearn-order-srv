import grpc
import asyncio
from grpc import aio
from tenacity import RetryError
from src.shared.utils.get_metadata import get_metadata_value
from src.domain.exceptions.exceptions import DomainException
from src.application.dtos.get_order_dto import GetOrderDto
from src.application.dtos.get_orders_by_user_dto import GetOrdersByUserDto
from src.application.use_cases.order.get_order_use_case import GetOrderUseCase
from src.application.use_cases.order.get_orders_use_case import GetOrdersUseCase
from src.application.interfaces.logging_interface import ILoggingService
from src.application.interfaces.metrics_interface import IMetricsService
from src.application.interfaces.tracing_interface import ITracingService
from src.infrastructure.observability.logging_service import LoggingService
from src.application.dtos.order_create_dto import OrderCreateDto
from pydantic import ValidationError
from src.application.dtos.session_booking_create_dto import SessionBookingCreateDTO
from src.application.use_cases.session_booking.session_booking_use_case import BookSessionUseCase
from src.infrastructure.grpc.auth_guard import AuthGuard
from src.infrastructure.grpc.generated.order_service_pb2 import (
    GetOrderByIdRequest,
    GetOrderByUserIdRequest,
    OrderResponse,
    OrderSuccess,
    OrdersResponse,
    BookSessionResponse,
    OrdersSuccess,
    PlaceOrderSuccess,
    BookSessionSuccess,
    Error,
    ErrorDetail
)
from src.infrastructure.grpc.generated.order_service_pb2_grpc import OrderServiceServicer, add_OrderServiceServicer_to_server
from src.application.use_cases.order.place_order_use_case import PlaceOrderUseCase
from src.infrastructure.grpc.interceptors.server_interceptor import (
    ServerLoggingInterceptor,
    ServerMetricsInterceptor,
    ServerTracingInterceptor,
    ServerAuthInterceptor,
)
from src.infrastructure.config.settings import settings


class OrderServiceImpl(OrderServiceServicer):
    def __init__(self,
                 place_order_use_case: PlaceOrderUseCase,
                 get_order_use_case: GetOrderUseCase,
                 get_orders_use_case: GetOrdersUseCase,
                 book_session_use_case: BookSessionUseCase,
                 logger: ILoggingService
                 ):
        self.place_order_use_case = place_order_use_case
        self.get_order_use_case = get_order_use_case
        self.get_orders_use_case = get_orders_use_case
        self.book_session_use_case = book_session_use_case
        self.logger = logger.get_logger("OrderServiceImpl")

    def _create_error_response(self, code: str, message: str, details: list | None = None) -> Error:
        """Create a structured error response"""
        error_details = []
        if details:
            for detail in details:
                error_details.append(ErrorDetail(
                    field=detail.get('field', ''),
                    message=detail.get('message', '')
                ))

        return Error(
            code=code,
            message=message,
            details=error_details
        )

    async def PlaceOrder(self, request, context: aio.ServicerContext):
        self.logger.info(
            f"Received PlaceOrder request for user {request.user_id}")
        try:
            self.logger.info("place order request " + str(request))
            # The proto defines optional coupon as `coupon_code`; map it to DTO's coupon_id
            coupon_code = request.coupon_code if hasattr(
                request, 'coupon_code') and request.coupon_code else None
            order_dto = OrderCreateDto(
                user_id=request.user_id,
                coupon_code=coupon_code,
                course_ids=list(request.course_ids),
            )
            auth_token = get_metadata_value(
                context, "authorization", strip_prefix="Bearer ")
            idempotency_key = get_metadata_value(
                context, "idempotency-key", cast=lambda x: str(x))
            self.logger.info("Idempotency Key metadata " +
                             str(idempotency_key))

            result = await self.place_order_use_case.execute(order_dto, idempotency_key)
            self.logger.info(f"Order {result.id} placed successfully")
            return OrderResponse(
                success=OrderSuccess(order=result.to_response_data())
            )
        except RetryError as retry_error:
            actual_exception = retry_error.last_attempt.exception()
            if isinstance(actual_exception, DomainException):
                return OrderResponse(
                    error=self._create_error_response(
                        code=type(actual_exception).__name__,
                        message=str(actual_exception),
                        details=[{"field": "request",
                                  "message": str(actual_exception)}]
                    )
                )
            else:
                # fallback to generic error
                return OrderResponse(
                    error=self._create_error_response(
                        code="INTERNAL",
                        message="Failed to place order",
                        details=[{"field": "service",
                                  "message": str(retry_error)}]
                    )
                )
        except DomainException as e:
            return OrderResponse(
                error=self._create_error_response(
                    code=type(e).__name__,
                    message=str(e),
                    details=[{"field": "request", "message": str(e)}]
                )
            )
        except ValidationError as ve:
            details = []
            for err in ve.errors():
                field_path = ".".join(str(p) for p in err.get("loc", []))
                details.append({
                    "field": field_path or "request",
                    "message": err.get("msg", "Invalid value"),
                })
            self.logger.error(f"Validation error in PlaceOrder: {ve}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INVALID_ARGUMENT",
                    message="Invalid request data",
                    details=details,
                )
            )

        except Exception as e:
            self.logger.error(f"Failed to place order: {str(e)}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INTERNAL",
                    message="Failed to place order",
                    details=[{"field": "service", "message": str(e)}]
                )
            )

    async def GetOrderById(self, request, context: aio.ServicerContext):
        self.logger.info(
            f"Received GetOrderById request for user {request.order_id}")
        try:
            order_dto = GetOrderDto(
                order_id=request.order_id)
            result = await self.get_order_use_case.execute(order_dto)
            self.logger.info(f"fetched order with id {request.order_id}")
            return OrderResponse(
                success=OrderSuccess(order=result.to_response_data())

            )
        except RetryError as retry_error:
            actual_exception = retry_error.last_attempt.exception()
            if isinstance(actual_exception, DomainException):
                return OrderResponse(
                    error=self._create_error_response(
                        code=type(actual_exception).__name__,
                        message=str(actual_exception),
                        details=[{"field": "request",
                                  "message": str(actual_exception)}]
                    )
                )
            else:
                # fallback to generic error
                return OrderResponse(
                    error=self._create_error_response(
                        code="INTERNAL",
                        message="Failed to get order",
                        details=[{"field": "service",
                                  "message": str(retry_error)}]
                    )
                )
        except DomainException as e:
            return OrderResponse(
                error=self._create_error_response(
                    code=type(e).__name__,
                    message=str(e),
                    details=[{"field": "request", "message": str(e)}]
                )
            )
        except ValidationError as ve:
            details = []
            for err in ve.errors():
                field_path = ".".join(str(p) for p in err.get("loc", []))
                details.append({
                    "field": field_path or "request",
                    "message": err.get("msg", "Invalid value"),
                })
            self.logger.error(f"Validation error in PlaceOrder: {ve}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INVALID_ARGUMENT",
                    message="Invalid request data",
                    details=details,
                )
            )

        except Exception as e:
            self.logger.error(f"Failed to get order: {str(e)}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INTERNAL",
                    message="Failed to get order",
                    details=[{"field": "service", "message": str(e)}]
                )
            )

    async def GetOrdersByUserId(self, request, context: aio.ServicerContext):
        self.logger.info(
            f"Received GetOrdersByUserId request for user {request.user_id}")
        try:
            order_dto = GetOrdersByUserDto(
                user_id=request.user_id)
            result = await self.get_orders_use_case.execute(order_dto)
            self.logger.info(f"Fetched orders for user  {request.user_id}")
            return OrdersResponse(
                success=OrdersSuccess(
                    orders=[order.to_response_data() for order in result])
            )
        except RetryError as retry_error:
            actual_exception = retry_error.last_attempt.exception()
            if isinstance(actual_exception, DomainException):
                return OrderResponse(
                    error=self._create_error_response(
                        code=type(actual_exception).__name__,
                        message=str(actual_exception),
                        details=[{"field": "request",
                                  "message": str(actual_exception)}]
                    )
                )
            else:
                # fallback to generic error
                return OrderResponse(
                    error=self._create_error_response(
                        code="INTERNAL",
                        message="Failed to get orders",
                        details=[{"field": "service",
                                  "message": str(retry_error)}]
                    )
                )
        except DomainException as e:
            return OrderResponse(
                error=self._create_error_response(
                    code=type(e).__name__,
                    message=str(e),
                    details=[{"field": "request", "message": str(e)}]
                )
            )
        except ValidationError as ve:
            details = []
            for err in ve.errors():
                field_path = ".".join(str(p) for p in err.get("loc", []))
                details.append({
                    "field": field_path or "request",
                    "message": err.get("msg", "Invalid value"),
                })
            self.logger.error(f"Validation error in PlaceOrder: {ve}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INVALID_ARGUMENT",
                    message="Invalid request data",
                    details=details,
                )
            )

        except Exception as e:
            self.logger.error(f"Failed to get orders by userId: {str(e)}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INTERNAL",
                    message="Failed to get orders by userId",
                    details=[{"field": "service", "message": str(e)}]
                )
            )

    async def BookSession(self, request, context: aio.ServicerContext):
        self.logger.info(
            f"Received BookSession request for user {request.user_id}")
        try:
            booking_dto = SessionBookingCreateDTO(
                user_id=request.user_id, session_id=request.session_id)
            result = await self.book_session_use_case.execute(booking_dto)
            self.logger.info(
                f"Session booking {result.id} created successfully")
            return BookSessionResponse(
                success=BookSessionSuccess(
                    id=result.id,
                    user_id=result.user_id,
                    session_id=result.session_id,
                    amount=result.amount,
                    currency=result.currency,
                    status=result.status,
                    created_at=result.created_at.isoformat(),
                    updated_at=result.updated_at.isoformat(),
                )
            )
        except DomainException as e:
            return OrderResponse(
                error=self._create_error_response(
                    code=type(e).__name__,
                    message=str(e),
                    details=[{"field": "request", "message": str(e)}]
                )
            )
        except ValidationError as ve:
            details = []
            for err in ve.errors():
                field_path = ".".join(str(p) for p in err.get("loc", []))
                details.append({
                    "field": field_path or "request",
                    "message": err.get("msg", "Invalid value"),
                })
            self.logger.error(f"Validation error in PlaceOrder: {ve}")
            return OrderResponse(
                error=self._create_error_response(
                    code="INVALID_ARGUMENT",
                    message="Invalid request data",
                    details=details,
                )
            )

        except Exception as e:
            self.logger.error(f"Failed to book session: {str(e)}")
            return BookSessionResponse(
                error=self._create_error_response(
                    code="INTERNAL",
                    message="Failed to book session",
                    details=[{"field": "service", "message": str(e)}]
                )
            )


async def start_grpc_server(
    place_order_use_case: PlaceOrderUseCase,
    book_session_use_case: BookSessionUseCase,
    get_order_use_case: GetOrderUseCase,
    get_orders_use_case: GetOrdersUseCase,
    auth_guard: AuthGuard,
    logger_service: ILoggingService,
    metrics: IMetricsService,
    tracer: ITracingService,
):
    server = aio.server(
        interceptors=[
            ServerLoggingInterceptor(logger_service),
            ServerMetricsInterceptor(logger=logger_service, metrics=metrics),
            ServerTracingInterceptor(),
            # ServerAuthInterceptor(auth_guard, logger_service),
        ]
    )
    add_OrderServiceServicer_to_server(
        OrderServiceImpl(place_order_use_case,
                         get_order_use_case,
                         get_orders_use_case,
                         book_session_use_case, logger_service), server
    )
    logger = logger_service.get_logger("start_grpc_server")
    server.add_insecure_port(f'[::]:{settings.GRPC_PORT}')
    logger.info(f"Starting gRPC server on port {settings.GRPC_PORT}")
    await server.start()
    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        logger.info(
            "gRPC server cancellation received; initiating graceful shutdown")
        raise
    finally:
        # Ensure server is stopped before the event loop closes to avoid warnings
        await server.stop(grace=1)
