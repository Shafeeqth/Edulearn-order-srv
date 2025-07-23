from datetime import datetime

from pydantic import BaseModel


class OrderDto(BaseModel):
    id: str
    user_id: str
    course_ids: list[str]
    total_amount: float
    currency: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
