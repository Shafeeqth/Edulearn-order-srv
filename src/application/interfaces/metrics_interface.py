from abc import ABC, abstractmethod

class MetricsInterface(ABC):
    @abstractmethod
    def setup_metrics(self) -> None:
        pass

    @abstractmethod
    def request_counter(self, method: str, endpoint: str, status: str) -> None:
        pass

    @abstractmethod
    def request_latency(self, method: str, endpoint: str, latency: float) -> None:
        pass

    @abstractmethod
    def active_orders(self, count: int) -> None:
        pass

    @abstractmethod
    def cache_hits(self, type: str) -> None:
        pass

    @abstractmethod
    def cache_misses(self, type: str) -> None:
        pass

    @abstractmethod
    def saga_failures(self, step: str) -> None:
        pass