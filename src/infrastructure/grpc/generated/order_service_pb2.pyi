from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("code", "message", "details")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    details: _containers.RepeatedCompositeFieldContainer[ErrorDetail]
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., details: _Optional[_Iterable[_Union[ErrorDetail, _Mapping]]] = ...) -> None: ...

class ErrorDetail(_message.Message):
    __slots__ = ("field", "message")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    field: str
    message: str
    def __init__(self, field: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class OrderItemsData(_message.Message):
    __slots__ = ("course_id", "price")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    price: float
    def __init__(self, course_id: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...

class PaymentDetailsData(_message.Message):
    __slots__ = ("payment_id", "provider", "provider_order_id", "payment_status", "updated_at")
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    payment_id: str
    provider: str
    provider_order_id: str
    payment_status: str
    updated_at: str
    def __init__(self, payment_id: _Optional[str] = ..., provider: _Optional[str] = ..., provider_order_id: _Optional[str] = ..., payment_status: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class MoneyData(_message.Message):
    __slots__ = ("price", "currency", "discount", "sub_total")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    SUB_TOTAL_FIELD_NUMBER: _ClassVar[int]
    price: float
    currency: str
    discount: float
    sub_total: float
    def __init__(self, price: _Optional[float] = ..., currency: _Optional[str] = ..., discount: _Optional[float] = ..., sub_total: _Optional[float] = ...) -> None: ...

class OrderData(_message.Message):
    __slots__ = ("id", "user_id", "items", "payment_details", "amount", "status", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    items: _containers.RepeatedCompositeFieldContainer[OrderItemsData]
    payment_details: PaymentDetailsData
    amount: MoneyData
    status: str
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[OrderItemsData, _Mapping]]] = ..., payment_details: _Optional[_Union[PaymentDetailsData, _Mapping]] = ..., amount: _Optional[_Union[MoneyData, _Mapping]] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class PlaceOrderSuccess(_message.Message):
    __slots__ = ("id", "user_id", "course_ids", "total_amount", "currency", "status", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_IDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    course_ids: _containers.RepeatedScalarFieldContainer[str]
    total_amount: float
    currency: str
    status: str
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., course_ids: _Optional[_Iterable[str]] = ..., total_amount: _Optional[float] = ..., currency: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class BookSessionSuccess(_message.Message):
    __slots__ = ("id", "user_id", "session_id", "amount", "currency", "status", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    session_id: str
    amount: float
    currency: str
    status: str
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., amount: _Optional[float] = ..., currency: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class PlaceOrderRequest(_message.Message):
    __slots__ = ("user_id", "coupon_code", "course_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COUPON_CODE_FIELD_NUMBER: _ClassVar[int]
    COURSE_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    coupon_code: str
    course_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., coupon_code: _Optional[str] = ..., course_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class OrdersSuccess(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderData]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderData, _Mapping]]] = ...) -> None: ...

class OrderSuccess(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: OrderData
    def __init__(self, order: _Optional[_Union[OrderData, _Mapping]] = ...) -> None: ...

class OrderResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: OrderSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[OrderSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class OrdersResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: OrdersSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[OrdersSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class BookSessionRequest(_message.Message):
    __slots__ = ("user_id", "session_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_id: str
    def __init__(self, user_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetOrderByIdRequest(_message.Message):
    __slots__ = ("order_id", "user_id")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    user_id: str
    def __init__(self, order_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetOrderByUserIdRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class BookSessionResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: BookSessionSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[BookSessionSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
