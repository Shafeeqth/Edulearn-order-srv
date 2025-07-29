from datetime import datetime

from pydantic import BaseModel


class SessionBookingDTO(BaseModel):
    id: str
    user_id: str
    session_id: str
    amount: float
    currency: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
