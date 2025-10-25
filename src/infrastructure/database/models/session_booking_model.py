from typing import cast
from sqlalchemy import Column, Index, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

from src.application.dtos.session_booking_dto import SessionBookingDTO
from src.domain.entities.session_booking import SessionBooking
from src.infrastructure.database.database import Base
from src.domain.value_objects.money import Money


class SessionBookingModel(Base):
    __tablename__ = "session_bookings"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="INR")
    status = Column(String, default="PENDING")
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    version = Column(Integer, default=1)  # For optimistic locking

    # Indexes for common queries
    __table_args__ = (
        Index("idx_session_bookings_session_id_status", "session_id", "status"),
        Index("idx_session_bookings_user_id", "user_id"),
    )
    
    def map_to_domain1(self) -> SessionBooking:
        from sqlalchemy.inspection import inspect

        domain_data = {
            c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs
        }

        order = cast(SessionBooking, domain_data)
        return SessionBooking(**domain_data)
    

    def map_to_domain(self) -> SessionBooking:
        return SessionBooking(
           id=self.__dict__["id"],
            user_id=self.__dict__["user_id"],
            session_id=self.__dict__["session_id"],
            amount=Money(amount=self.__dict__["amount"], currency=self.__dict__["currency"]),
            status=self.__dict__["status"],
            created_at=self.__dict__["created_at"],
            updated_at=self.__dict__["updated_at"],
            version=self.__dict__["version"],
        )
    
    @classmethod
    def from_domain(cls, session_booking: SessionBooking) -> "SessionBookingModel":
        return cls(
            id=session_booking.id,
            user_id=session_booking.user_id,
            session_id=session_booking.session_id,
            amount=session_booking.amount.amount,
            currency=session_booking.amount.currency,
            status=session_booking.status,
            created_at=session_booking.created_at,
            updated_at=session_booking.updated_at,
            version=session_booking.version,
        )
