from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Literal
from uuid import uuid4

from src.domain.value_objects.money import Money


class OrderStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


Order_Status = Literal["PENDING", "COMPLETED", "FAILED"]


@dataclass
class Order:
    id: str
    user_id: str
    course_ids: list[str]
    total_amount: Money
    status: OrderStatus
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(
        cls, user_id: str, course_ids: list[str], total_amount: Money
    ) -> "Order":
        return cls(
            id=str(uuid4()),
            user_id=user_id,
            course_ids=course_ids,
            total_amount=total_amount,
            status=OrderStatus.PENDING,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

    def mark_completed(self):
        self.status = "COMPLETED"
        self.updated_at = datetime.now(timezone.utc)

    def mark_failed(self):
        self.status = "FAILED"
        self.updated_at = datetime.now(timezone.utc)
