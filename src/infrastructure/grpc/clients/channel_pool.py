from collections import deque
import logging
from grpc import aio

from src.application.interfaces.logging_interface import ILoggingService
from src.infrastructure.config.settings import settings


class ChannelPool:
    def __init__(
        self,
        service_name: str,
        service_port: int,
        logging_service: ILoggingService,
        max_size: int = 10,
    ) -> None:
        self.service_name = service_name
        self.service_port = service_port
        self.max_size = max_size
        self.pool: deque = deque(maxlen=max_size)
        self.logger = logging_service.get_logger("ChannelPool")
        self._initialize_pool()

    def _initialize_pool(self):
        for _ in range(self.max_size):
            # Prefer explicit host if provided, else use service name (useful in k8s)
            host = settings.USER_SERVICE_HOST if self.service_name == settings.USER_SERVICE_NAME else self.service_name
            channel = aio.insecure_channel(f"{host}:{self.service_port}")
            self.pool.append(channel)
        self.logger.info(
            f"Initialized channel pool for {self.service_name} with port {self.service_port} {self.max_size} channels"
        )

    async def acquire(self) -> aio.Channel:
        if not self.pool:
            self.logger.warning(
                f"Not available channels in pool for {self.service_name}, creating new channel")
            return aio.insecure_channel(f"{self.service_name}:{self.service_port}")
        channel = self.pool.popleft()
        return channel

    async def release(self, channel: aio.Channel):
        if len(self.pool) < self.max_size:
            self.pool.append(channel)
        else:
            await channel.close()
            self.logger.debug(
                f"Channel pool {self.service_name} is full, closed excess channel")

    async def close(self):
        while self.pool:
            channel = self.pool.popleft()
            await channel.close()
        self.logger.info(
            f"Closed all channels in pool for {self.service_name} port {self.service_port}")
