from abc import ABC, abstractmethod

class UserServiceClientInterface(ABC):
    @abstractmethod
    async def verify_user(self, user_id: str, token: str | bytes) -> dict:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

class CourseServiceClientInterface(ABC):
    @abstractmethod
    async def get_course(self, course_id: str) -> dict:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

class SessionServiceClientInterface(ABC):
    @abstractmethod
    async def get_session(self, session_id: str) -> dict:
        pass

    @abstractmethod
    async def get_available_slots(self, session_id: str) -> int:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass