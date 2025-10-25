from abc import ABC, abstractmethod

class IAuthGuard(ABC):
    @abstractmethod
    async def validate_token(self, token: str) -> dict:
        pass

    @abstractmethod
    async def authorize(self, user_info: dict, required_role: str) -> None:
        pass