from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.session_booking import SessionBooking

class ISessionBookingRepository(ABC):
    @abstractmethod
    async def save(self, booking: SessionBooking) -> None:
        pass

    @abstractmethod
    async def find_by_id(self, booking_id: str) -> Optional[SessionBooking]:
        pass

    @abstractmethod
    async def find_by_user_id(self, user_id: str) -> List[SessionBooking]:
        pass

    @abstractmethod
    async def count_bookings_for_session(self, session_id: str) -> int:
        pass
    
    @abstractmethod
    async def find_by_session_id(self, session_id: str) -> list[SessionBooking]:
        pass