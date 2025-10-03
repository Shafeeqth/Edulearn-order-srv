from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class GetOrderDto(BaseModel):
    order_id: str = Field(..., description="ID of the order is required")

