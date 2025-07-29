from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import structlog

class LoggingInterface(ABC):
    @abstractmethod
    def get_logger(self, name: str) -> "structlog.stdlib.BoundLogger":
        pass
    
    @abstractmethod
    def setup_logger(self) -> "structlog.stdlib.BoundLogger":
        pass
    
    @abstractmethod
    def bind_context(self, **kwargs: Any) -> "structlog.stdlib.BoundLogger":
        pass
    
    @abstractmethod
    def unbind_context(self, *keys: str) -> "structlog.stdlib.BoundLogger":
        pass