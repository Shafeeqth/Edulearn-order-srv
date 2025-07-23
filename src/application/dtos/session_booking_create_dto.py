from pydantic import BaseModel, Field, validator


class SessionBookingCreateDTO(BaseModel):
    user_id: str = Field(..., description="ID of the user booking the session")
    session_id: str = Field(..., description="ID of the session to book")

    @validator("session_id")
    def validate_session_id(cls, value):
        if not value.strip():
            raise ValueError("Session ID must be a non-empty string")
        return value
