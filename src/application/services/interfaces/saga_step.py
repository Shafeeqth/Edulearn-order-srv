from abc import ABC, abstractmethod
from typing import Any


class SagaStep(ABC):
    @abstractmethod
    async def execute(self, context: dict[str, Any]) -> None:
        pass
    
    @abstractmethod
    async def compensate(self, context: dict[str, Any]) -> None:
        pass
    
    