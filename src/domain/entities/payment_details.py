from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Any

PaymentStatus = Literal["pending", "success",
                        "failed", "refunded", "expired"]

# class PaymentStatus(str, Enum):
#     PENDING = "pending"
#     PENDING = "pending"
#     SUCCESS = "success"
#     FAILED = "failed"
#     REFUNDED = "refunded"
#     EXPIRED = "expired"


@dataclass
class PaymentDetails:
    payment_id: str
    provider: str
    provider_order_id: str
    payment_status: PaymentStatus = "pending"
    updated_at: datetime = datetime.now()

    @classmethod
    def create(
        cls,
        payment_id: str,
        provider: str,
        provider_order_id: str,
        payment_status: PaymentStatus = "pending"
    ) -> "PaymentDetails":
        return cls(
            payment_id,
            provider,
            provider_order_id,
            payment_status,

        )
    def setStatus(self, status: PaymentStatus):
        self.payment_status = status
        self.updated_at = datetime.now()

    def to_dict(self) -> dict[str, Any]:
        return {
            "payment_id": self.payment_id,
            "provider": self.provider,
            "provider_order_id": self.provider_order_id,
            "payment_status": self.payment_status,
            "updated_at": self.updated_at,
        }
