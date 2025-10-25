import grpc
from grpc import aio

from src.infrastructure.config.settings import settings
from src.application.interfaces.logging_interface import ILoggingService
from src.infrastructure.grpc.interceptors.client_inerceptors import ClientAuthInterceptor, ClientTracingInterceptor
from src.infrastructure.grpc.generated.course_service_pb2 import GetCourseRequest, GetCoursesByIdsRequest
from src.infrastructure.grpc.generated.course_service_pb2_grpc import CourseServiceStub
from src.application.interfaces.grpc_client_interface import ICourseServiceClient
from src.infrastructure.grpc.clients.channel_pool import ChannelPool
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from circuitbreaker import circuit


class CourseServiceClient(ICourseServiceClient):
    def __init__(self, logging_service: ILoggingService, token: str | None = None):
        self.pool = ChannelPool(
            settings.COURSE_SERVICE_HOST, settings.COURSE_SERVICE_PORT, logging_service=logging_service, max_size=10)
        self.logger = logging_service.get_logger("CourseServiceClient")
        self.interceptors = [
            ClientTracingInterceptor(),
            # ClientAuthInterceptor(token) if token else None,
        ]
        self.interceptors = [i for i in self.interceptors if i is not None]

    @circuit(failure_threshold=5, recovery_timeout=30)
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def get_course(self, course_id: str) -> dict:
        channel = await self.pool.acquire()
        try:
            from typing import Any, cast
            intercept_fn = getattr(aio, "intercept_channel", None)
            if callable(intercept_fn):
                intercepted = cast(Any, intercept_fn)(
                    channel, *self.interceptors)
            else:
                intercepted = channel
            stub = CourseServiceStub(intercepted)
            request = GetCourseRequest(course_id=course_id)
            response = await stub.GetCourse(request)
            has_error = False
            if hasattr(response, "HasField"):
                try:
                    # type: ignore[attr-defined]
                    has_error = response.HasField("error")
                except Exception:
                    has_error = False
            else:
                err = getattr(response, "error", None)
                err_code = getattr(err, "code", "") if err is not None else ""
                err_msg = getattr(
                    err, "message", "") if err is not None else ""
                has_error = bool(err_code or err_msg)

            if has_error:
                err = getattr(response, "error", None)
                self.logger.error(
                    f"Failed to get course {course_id}: {getattr(err, 'message', '')}")
                raise ValueError(getattr(err, "message", "Unknown error"))

            return {"course_id": response.course.id, "price": response.course.price}
        except Exception as e:
            self.logger.error(f"Failed to get course {course_id}: {str(e)}")
            raise
        finally:
            await self.pool.release(channel)

    @circuit(failure_threshold=5, recovery_timeout=30)
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def get_courses_by_ids(self, course_ids: list[str]) -> list[dict]:
        channel = await self.pool.acquire()
        try:
            intercepted_channel = grpc.intercept_channel(
                channel, *self.interceptors)
            stub = CourseServiceStub(intercepted_channel)
            request = GetCoursesByIdsRequest(course_ids=course_ids)
            response = await stub.GetCourse(request)
            if response.error:
                self.logger.error(
                    f"Failed to get courses for {len(course_ids)} courses : {response.error}")
                raise ValueError(response.error)
            self.logger.info("courses ids response " + str(response))
            return [{"course_id": response.course_id, "price": response.price}]
        except Exception as e:
            self.logger.error(
                f"Failed to get {len(course_ids)} courses with: {str(e)}")
            raise
        finally:
            await self.pool.release(channel)

    async def close(self):
        await self.pool.close()
