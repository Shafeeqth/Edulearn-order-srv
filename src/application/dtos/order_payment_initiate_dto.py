from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class OrderPaymentInitiatedDto(BaseModel):
    order_id: str = Field(..., description="ID of the payment is required")
    payment_id: str = Field(..., description="Payment Id of the payment is required")
    provider: str = Field(..., description="Provider of the payment is required")
    provider_order_id: str = Field(..., description="Provider order Id  of the payment is required")
    payment_status: str = Field(..., description="status of the payment is required")
    created_at: str = Field(..., description="created at of the payment is required")

