import json
import functools
import hashlib
from typing import Any, Callable, Coroutine, Optional, TypeVar, ParamSpec
from src.infrastructure.redis.redis_client import RedisClient
from src.application.interfaces.logging_interface import ILoggingService

P = ParamSpec("P")
R = TypeVar("R")

class CacheService:
    def __init__(self, redis_client: RedisClient, logger: ILoggingService):
        self.redis = redis_client
        self.logger = logger.get_logger("CacheService")

    async def get_cache(self, key: str) -> Optional[Any]:
        try:
            cached_data = await self.redis.get(key)
            if cached_data:
                return json.loads(cached_data)
        except Exception as e:
            self.logger.error(f"Failed to get cache for key {key}: {e}")
        return None

    async def set_cache(self, key: str, value: Any, ttl: Optional[int] = None):
        try:
            await self.redis.set(key, json.dumps(value), expire=ttl)
        except Exception as e:
            self.logger.error(f"Failed to set cache for key {key}: {e}")

    async def invalidate_cache(self, pattern: str):
        """Invalidate cache keys matching the given pattern"""
        try:
            async for key in self.redis.client.scan_iter(match=f"{self.redis.key_prefix}{pattern}*"):
                await self.redis.client.delete(key)
                self.logger.debug(f"Invalidated cache: {key}")
        except Exception as e:
            self.logger.error(f"Failed to invalidate cache for pattern {pattern}: {e}")

    def _build_cache_key(self, prefix: str, args: tuple, kwargs: dict) -> str:
        raw_key = f"{prefix}:{json.dumps({'args': args, 'kwargs': kwargs}, sort_keys=True)}"
        hashed = hashlib.md5(raw_key.encode()).hexdigest()
        return f"{self.redis.key_prefix}{prefix}:{hashed}"

    def cache(
        self,
        prefix: str,
        ttl: Optional[int] = None,
        invalidate_patterns: Optional[list[str]] = None,
    ) -> Callable[[Callable[P, Coroutine[Any, Any, R]]], Callable[P, Coroutine[Any, Any, R]]]:
        """
        Decorator for caching async function results.
        Automatically invalidates related caches when needed.
        """

        def decorator(func: Callable[P, Coroutine[Any, Any, R]]):
            @functools.wraps(func)
            async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                cache_key = self._build_cache_key(prefix, args, kwargs)
                cached_result = await self.get_cache(cache_key)
                if cached_result is not None:
                    self.logger.debug(f"Cache hit: {cache_key}")
                    return cached_result

                self.logger.debug(f"Cache miss: {cache_key}")
                result = await func(*args, **kwargs)

                await self.set_cache(cache_key, result, ttl)

                # Invalidate dependent caches if configured
                if invalidate_patterns:
                    for pattern in invalidate_patterns:
                        await self.invalidate_cache(pattern)

                return result

            return wrapper

        return decorator

# from src.infrastructure.cache.cache_service import CacheService

# class CourseService:
#     def __init__(self, cache_service: CacheService):
#         self.cache_service = cache_service

#     @cache_service.cache(prefix="course:get_details", ttl=600)
#     async def get_course_details(self, course_id: str):
#         # Simulate a gRPC call or DB query
#         course = await self.grpc_client.get_course(course_id)
#         return course

#     async def update_course(self, course_id: str, data: dict):
#         # Perform update operation
#         updated = await self.grpc_client.update_course(course_id, data)

#         # Invalidate relevant caches
#         await self.cache_service.invalidate_cache(f"course:get_details:{course_id}")
#         return updated
# import functools
# import json
# from typing import Callable, Any, Optional
# from src.infrastructure.redis.redis_client import RedisClient
# from src.infrastructure.config.settings import settings

# def cache_key_builder(func: Callable, args: tuple, kwargs: dict) -> str:
#     key_base = f"{func.__module__}.{func.__qualname__}"
#     arg_part = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
#     return f"{key_base}:{hash(arg_part)}"

# def cacheable(ttl: Optional[int] = None):
#     """
#     Cache decorator that stores the result in Redis.
#     """
#     def decorator(func: Callable):
#         @functools.wraps(func)
#         async def wrapper(*args, **kwargs):
#             self = args[0] if args else None
#             redis_client: RedisClient = getattr(self, "redis", None)
#             if not redis_client:
#                 raise RuntimeError("Redis client not found on instance")

#             key = cache_key_builder(func, args[1:], kwargs)
#             cached_data = await redis_client.get(key)
#             if cached_data:
#                 self.logger.debug(f"Cache hit: {key}")
#                 return json.loads(cached_data)

#             result = await func(*args, **kwargs)
#             await redis_client.set(key, result, expire=ttl or settings.REDIS_TTL)
#             self.logger.debug(f"Cache set: {key}")
#             return result
#         return wrapper
#     return decorator


# def cache_evict(pattern: str):
#     """
#     Decorator to clear cache entries matching a given pattern.
#     Useful for invalidating data when it changes.
#     """
#     def decorator(func: Callable):
#         @functools.wraps(func)
#         async def wrapper(*args, **kwargs):
#             self = args[0] if args else None
#             redis_client: RedisClient = getattr(self, "redis", None)
#             if not redis_client:
#                 raise RuntimeError("Redis client not found on instance")

#             result = await func(*args, **kwargs)

#             async for key in redis_client.client.scan_iter(f"*{pattern}*"):
#                 await redis_client.delete(key)
#                 self.logger.debug(f"Cache invalidated: {key}")
#             return result
#         return wrapper
#     return decorator

