from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class GetOrdersByUserDto(BaseModel):
    user_id: str = Field(..., description="ID of the user is required")

