from dataclasses import dataclass
from typing import Any


@dataclass
class OrderItem:
    course_id: str
    price: float

    @classmethod
    def create(
        cls, course_id: str, price: float
    ) -> "OrderItem":
        return cls(
            course_id=course_id,
            price=price,
        )

    def to_dict(self) -> dict[str, Any]:
        return {"course_id": self.course_id, "price": self.price}
