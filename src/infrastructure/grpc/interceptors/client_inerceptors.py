import grpc
from grpc import aio
from opentelemetry import trace, propagate
from typing import Any, Tuple, Any as _Any


MetadataType = _Any


class _ClientCallDetails:
    def __init__(
        self,
        method: str,
        timeout: float | None,
        metadata: MetadataType,
        credentials: grpc.CallCredentials | None,
        wait_for_ready: bool | None,
        compression: grpc.Compression | None,
    ) -> None:
        self.method = method
        self.timeout = timeout
        self.metadata = metadata
        self.credentials = credentials
        self.wait_for_ready = wait_for_ready
        self.compression = compression


class ClientTracingInterceptor(aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(self, continuation, client_call_details, request):
        tracer = trace.get_tracer(__name__)
        with tracer.start_as_current_span(
            client_call_details.method,
            kind=trace.SpanKind.CLIENT,
        ) as span:
            span.set_attribute("grpc.method", client_call_details.method)

            # Inject span context into metadata
            md_dict = dict(client_call_details.metadata or [])
            propagate.inject(md_dict)
            new_details = _ClientCallDetails(
                method=client_call_details.method,
                timeout=client_call_details.timeout,
                metadata=tuple((k, v) for k, v in md_dict.items()),
                credentials=client_call_details.credentials,
                wait_for_ready=getattr(
                    client_call_details, "wait_for_ready", None),
                compression=getattr(client_call_details, "compression", None),
            )
            return await continuation(new_details, request)  # type: ignore[arg-type]


class ClientAuthInterceptor(aio.UnaryUnaryClientInterceptor):
    def __init__(self, token: str):
        self.token = token

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        md_dict = dict(client_call_details.metadata or [])
        md_dict["authorization"] = f"Bearer {self.token}"
        new_details = _ClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            metadata=tuple((k, v) for k, v in md_dict.items()),
            credentials=client_call_details.credentials,
            wait_for_ready=getattr(client_call_details,
                                   "wait_for_ready", None),
            compression=getattr(client_call_details, "compression", None),
        )
        return await continuation(new_details, request)  # type: ignore[arg-type]
