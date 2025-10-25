from abc import ABC, abstractmethod


class IUserServiceClient(ABC):
    @abstractmethod
    async def get_user(self, user_id: str) -> dict:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass


class ICourseServiceClient(ABC):
    @abstractmethod
    async def get_course(self, course_id: str) -> dict:
        pass

    @abstractmethod
    async def get_courses_by_ids(self, course_ids: list[str]) -> list[dict]:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass


class ISessionServiceClient(ABC):
    @abstractmethod
    async def get_session(self, session_id: str) -> dict:
        pass

    @abstractmethod
    async def get_available_slots(self, session_id: str) -> int:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass
