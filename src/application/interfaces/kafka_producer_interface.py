from abc import ABC, abstractmethod
from fastavro.types import Schema

class KafkaProducerInterface(ABC):
    @abstractmethod
    async def publish_event(self, topic: str, event: dict, schema: Schema) -> None:
        pass
    
    @abstractmethod
    async def start(self) -> None:
        pass

    @abstractmethod
    async def stop(self) -> None:
        pass
        
        