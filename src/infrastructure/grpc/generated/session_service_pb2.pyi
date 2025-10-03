from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class GetSessionResponse(_message.Message):
    __slots__ = ("session_id", "price", "max_slots", "error")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    MAX_SLOTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    price: float
    max_slots: int
    error: str
    def __init__(self, session_id: _Optional[str] = ..., price: _Optional[float] = ..., max_slots: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...

class GetAvailableSlotsRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class GetAvailableSlotsResponse(_message.Message):
    __slots__ = ("available_slots", "error")
    AVAILABLE_SLOTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    available_slots: int
    error: str
    def __init__(self, available_slots: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
