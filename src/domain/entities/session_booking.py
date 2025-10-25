from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

from src.domain.value_objects.money import Money

Session_Status = Literal["PENDING", "CONFIRMED", "CANCELLED"]


@dataclass
class SessionBooking:
    id: str
    user_id: str
    session_id: str
    amount: Money
    status: Session_Status
    created_at: datetime
    updated_at: datetime
    version: int  # For optimistic locking

    @classmethod
    def create(cls, user_id: str, session_id: str, amount: Money) -> "SessionBooking":
        return cls(
            id=str(uuid4()),
            user_id=user_id,
            session_id=session_id,
            amount=amount,
            status="PENDING",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            version=1,
        )

    def confirm(self):
        self.status = "CONFIRMED"
        self.updated_at = datetime.now(timezone.utc)
        self.version += 1

    def cancel(self):
        self.status = "CANCELLED"
        self.updated_at = datetime.now(timezone.utc)
        self.version += 1
