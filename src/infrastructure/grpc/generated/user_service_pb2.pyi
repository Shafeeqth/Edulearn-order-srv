from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserProfileData(_message.Message):
    __slots__ = ("bio", "phone", "country", "city", "gender", "preference", "language", "website")
    BIO_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    bio: str
    phone: str
    country: str
    city: str
    gender: str
    preference: str
    language: str
    website: str
    def __init__(self, bio: _Optional[str] = ..., phone: _Optional[str] = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., gender: _Optional[str] = ..., preference: _Optional[str] = ..., language: _Optional[str] = ..., website: _Optional[str] = ...) -> None: ...

class UserSocialsData(_message.Message):
    __slots__ = ("provider", "profile_url", "provider_user_url")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_USER_URL_FIELD_NUMBER: _ClassVar[int]
    provider: str
    profile_url: str
    provider_user_url: str
    def __init__(self, provider: _Optional[str] = ..., profile_url: _Optional[str] = ..., provider_user_url: _Optional[str] = ...) -> None: ...

class InstructorProfileData(_message.Message):
    __slots__ = ("bio", "headline", "experience", "certificate", "tags", "expertise", "rating", "totalRatings", "totalCourses", "totalStudents")
    BIO_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EXPERTISE_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TOTALRATINGS_FIELD_NUMBER: _ClassVar[int]
    TOTALCOURSES_FIELD_NUMBER: _ClassVar[int]
    TOTALSTUDENTS_FIELD_NUMBER: _ClassVar[int]
    bio: str
    headline: str
    experience: str
    certificate: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    expertise: _containers.RepeatedScalarFieldContainer[str]
    rating: int
    totalRatings: int
    totalCourses: int
    totalStudents: int
    def __init__(self, bio: _Optional[str] = ..., headline: _Optional[str] = ..., experience: _Optional[str] = ..., certificate: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., expertise: _Optional[_Iterable[str]] = ..., rating: _Optional[int] = ..., totalRatings: _Optional[int] = ..., totalCourses: _Optional[int] = ..., totalStudents: _Optional[int] = ...) -> None: ...

class UserData(_message.Message):
    __slots__ = ("id", "email", "role", "firstName", "status", "lastName", "avatar", "lastLogin", "profile", "instructor_profile", "socials", "updatedAt", "createdAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    LASTLOGIN_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SOCIALS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    role: str
    firstName: str
    status: str
    lastName: str
    avatar: str
    lastLogin: str
    profile: UserProfileData
    instructor_profile: InstructorProfileData
    socials: _containers.RepeatedCompositeFieldContainer[UserSocialsData]
    updatedAt: str
    createdAt: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[str] = ..., firstName: _Optional[str] = ..., status: _Optional[str] = ..., lastName: _Optional[str] = ..., avatar: _Optional[str] = ..., lastLogin: _Optional[str] = ..., profile: _Optional[_Union[UserProfileData, _Mapping]] = ..., instructor_profile: _Optional[_Union[InstructorProfileData, _Mapping]] = ..., socials: _Optional[_Iterable[_Union[UserSocialsData, _Mapping]]] = ..., updatedAt: _Optional[str] = ..., createdAt: _Optional[str] = ...) -> None: ...

class PaginationRequest(_message.Message):
    __slots__ = ("page", "pageSize")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    pageSize: int
    def __init__(self, page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class PaginationResponse(_message.Message):
    __slots__ = ("totalItems", "totalPages")
    TOTALITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTALPAGES_FIELD_NUMBER: _ClassVar[int]
    totalItems: int
    totalPages: int
    def __init__(self, totalItems: _Optional[int] = ..., totalPages: _Optional[int] = ...) -> None: ...

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

class WalletTransaction(_message.Message):
    __slots__ = ("transactionId", "userId", "amount", "type", "transactionDate")
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONDATE_FIELD_NUMBER: _ClassVar[int]
    transactionId: str
    userId: str
    amount: float
    type: str
    transactionDate: str
    def __init__(self, transactionId: _Optional[str] = ..., userId: _Optional[str] = ..., amount: _Optional[float] = ..., type: _Optional[str] = ..., transactionDate: _Optional[str] = ...) -> None: ...

class CartData(_message.Message):
    __slots__ = ("id", "userId", "total", "items", "updated_at", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    userId: str
    total: int
    items: _containers.RepeatedCompositeFieldContainer[CartItemData]
    updated_at: str
    created_at: str
    def __init__(self, id: _Optional[str] = ..., userId: _Optional[str] = ..., total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[CartItemData, _Mapping]]] = ..., updated_at: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...

class CartItemData(_message.Message):
    __slots__ = ("id", "courseId", "createdAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    courseId: str
    createdAt: str
    def __init__(self, id: _Optional[str] = ..., courseId: _Optional[str] = ..., createdAt: _Optional[str] = ...) -> None: ...

class WishlistItemData(_message.Message):
    __slots__ = ("id", "courseId", "createdAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    courseId: str
    createdAt: str
    def __init__(self, id: _Optional[str] = ..., courseId: _Optional[str] = ..., createdAt: _Optional[str] = ...) -> None: ...

class WishlistData(_message.Message):
    __slots__ = ("id", "userId", "total", "items", "updated_at", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    userId: str
    total: int
    items: _containers.RepeatedCompositeFieldContainer[CartItemData]
    updated_at: str
    created_at: str
    def __init__(self, id: _Optional[str] = ..., userId: _Optional[str] = ..., total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[CartItemData, _Mapping]]] = ..., updated_at: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...

class AddToCartRequest(_message.Message):
    __slots__ = ("userId", "cartId", "courseId")
    USERID_FIELD_NUMBER: _ClassVar[int]
    CARTID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    cartId: str
    courseId: str
    def __init__(self, userId: _Optional[str] = ..., cartId: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class ToggleWishlistItemRequest(_message.Message):
    __slots__ = ("userId", "wishlistId", "courseId")
    USERID_FIELD_NUMBER: _ClassVar[int]
    WISHLISTID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    wishlistId: str
    courseId: str
    def __init__(self, userId: _Optional[str] = ..., wishlistId: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class ToggleCartItemRequest(_message.Message):
    __slots__ = ("userId", "cartId", "courseId")
    USERID_FIELD_NUMBER: _ClassVar[int]
    CARTID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    cartId: str
    courseId: str
    def __init__(self, userId: _Optional[str] = ..., cartId: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class AddToCartResponse(_message.Message):
    __slots__ = ("item", "error")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    item: CartItemData
    error: Error
    def __init__(self, item: _Optional[_Union[CartItemData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ToggleWishlistItemResponse(_message.Message):
    __slots__ = ("item", "error")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    item: WishlistItemData
    error: Error
    def __init__(self, item: _Optional[_Union[WishlistItemData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ToggleCartItemResponse(_message.Message):
    __slots__ = ("item", "error")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    item: CartItemData
    error: Error
    def __init__(self, item: _Optional[_Union[CartItemData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class RemoveFromCartRequest(_message.Message):
    __slots__ = ("cartId", "courseId")
    CARTID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    cartId: str
    courseId: str
    def __init__(self, cartId: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class RemoveFromCartResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: RemoveSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[RemoveSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class RemoveSuccess(_message.Message):
    __slots__ = ("removed",)
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    removed: bool
    def __init__(self, removed: bool = ...) -> None: ...

class ListCartRequest(_message.Message):
    __slots__ = ("userId", "pagination")
    USERID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    userId: str
    pagination: PaginationRequest
    def __init__(self, userId: _Optional[str] = ..., pagination: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class ListCartResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CartListSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[CartListSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class CartListSuccess(_message.Message):
    __slots__ = ("cart", "pagination")
    CART_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    cart: CartData
    pagination: PaginationResponse
    def __init__(self, cart: _Optional[_Union[CartData, _Mapping]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class WishlistListSuccess(_message.Message):
    __slots__ = ("wishlist", "pagination")
    WISHLIST_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    wishlist: WishlistData
    pagination: PaginationResponse
    def __init__(self, wishlist: _Optional[_Union[WishlistData, _Mapping]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class AddToWishlistRequest(_message.Message):
    __slots__ = ("userId", "wishlistId", "courseId")
    USERID_FIELD_NUMBER: _ClassVar[int]
    WISHLISTID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    wishlistId: str
    courseId: str
    def __init__(self, userId: _Optional[str] = ..., wishlistId: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class AddToWishlistResponse(_message.Message):
    __slots__ = ("item", "error")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    item: WishlistItemData
    error: Error
    def __init__(self, item: _Optional[_Union[WishlistItemData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class RemoveFromWishlistRequest(_message.Message):
    __slots__ = ("wishlistId", "courseId")
    WISHLISTID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    wishlistId: str
    courseId: str
    def __init__(self, wishlistId: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class RemoveFromWishlistResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: RemoveSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[RemoveSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ListWishlistRequest(_message.Message):
    __slots__ = ("userId", "pagination")
    USERID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    userId: str
    pagination: PaginationRequest
    def __init__(self, userId: _Optional[str] = ..., pagination: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class ListWishlistResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: WishlistSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[WishlistSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class WishlistSuccess(_message.Message):
    __slots__ = ("wishlist", "pagination")
    WISHLIST_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    wishlist: WishlistData
    pagination: PaginationResponse
    def __init__(self, wishlist: _Optional[_Union[WishlistData, _Mapping]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class InstructorSuccessResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: UserData
    def __init__(self, user: _Optional[_Union[UserData, _Mapping]] = ...) -> None: ...

class RegisterInstructorResponse(_message.Message):
    __slots__ = ("error", "success")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: Error
    success: InstructorSuccessResponse
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ..., success: _Optional[_Union[InstructorSuccessResponse, _Mapping]] = ...) -> None: ...

class RegisterInstructorRequest(_message.Message):
    __slots__ = ("userId", "extraEmail", "city", "firstName", "lastName", "expertise", "phone", "linkedin", "instagram", "facebook", "language", "website", "biography", "headline", "education", "experience", "country")
    USERID_FIELD_NUMBER: _ClassVar[int]
    EXTRAEMAIL_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    EXPERTISE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LINKEDIN_FIELD_NUMBER: _ClassVar[int]
    INSTAGRAM_FIELD_NUMBER: _ClassVar[int]
    FACEBOOK_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    BIOGRAPHY_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    userId: str
    extraEmail: str
    city: str
    firstName: str
    lastName: str
    expertise: str
    phone: str
    linkedin: str
    instagram: str
    facebook: str
    language: str
    website: str
    biography: str
    headline: str
    education: str
    experience: int
    country: str
    def __init__(self, userId: _Optional[str] = ..., extraEmail: _Optional[str] = ..., city: _Optional[str] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., expertise: _Optional[str] = ..., phone: _Optional[str] = ..., linkedin: _Optional[str] = ..., instagram: _Optional[str] = ..., facebook: _Optional[str] = ..., language: _Optional[str] = ..., website: _Optional[str] = ..., biography: _Optional[str] = ..., headline: _Optional[str] = ..., education: _Optional[str] = ..., experience: _Optional[int] = ..., country: _Optional[str] = ...) -> None: ...

class DetailedUserInfo(_message.Message):
    __slots__ = ("userId", "firstName", "lastName", "phone", "headline", "biography", "avatar", "website", "language", "facebook", "instagram", "linkedin", "status", "role", "email", "updatedAt", "createdAt")
    USERID_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    BIOGRAPHY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FACEBOOK_FIELD_NUMBER: _ClassVar[int]
    INSTAGRAM_FIELD_NUMBER: _ClassVar[int]
    LINKEDIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    userId: str
    firstName: str
    lastName: str
    phone: str
    headline: str
    biography: str
    avatar: str
    website: str
    language: str
    facebook: str
    instagram: str
    linkedin: str
    status: str
    role: str
    email: str
    updatedAt: str
    createdAt: str
    def __init__(self, userId: _Optional[str] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., phone: _Optional[str] = ..., headline: _Optional[str] = ..., biography: _Optional[str] = ..., avatar: _Optional[str] = ..., website: _Optional[str] = ..., language: _Optional[str] = ..., facebook: _Optional[str] = ..., instagram: _Optional[str] = ..., linkedin: _Optional[str] = ..., status: _Optional[str] = ..., role: _Optional[str] = ..., email: _Optional[str] = ..., updatedAt: _Optional[str] = ..., createdAt: _Optional[str] = ...) -> None: ...

class UpdateUserDetailsRequest(_message.Message):
    __slots__ = ("userId", "firstName", "lastName", "phone", "socials", "biography", "avatar", "website", "language", "city", "country", "gender")
    USERID_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    SOCIALS_FIELD_NUMBER: _ClassVar[int]
    BIOGRAPHY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    userId: str
    firstName: str
    lastName: str
    phone: str
    socials: _containers.RepeatedCompositeFieldContainer[UserSocialsData]
    biography: str
    avatar: str
    website: str
    language: str
    city: str
    country: str
    gender: str
    def __init__(self, userId: _Optional[str] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., phone: _Optional[str] = ..., socials: _Optional[_Iterable[_Union[UserSocialsData, _Mapping]]] = ..., biography: _Optional[str] = ..., avatar: _Optional[str] = ..., website: _Optional[str] = ..., language: _Optional[str] = ..., city: _Optional[str] = ..., country: _Optional[str] = ..., gender: _Optional[str] = ...) -> None: ...

class UpdateUserDetailsResponse(_message.Message):
    __slots__ = ("user", "error")
    USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    user: UserData
    error: Error
    def __init__(self, user: _Optional[_Union[UserData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ChangePasswordRequest(_message.Message):
    __slots__ = ("userId", "oldPassword", "newPassword")
    USERID_FIELD_NUMBER: _ClassVar[int]
    OLDPASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEWPASSWORD_FIELD_NUMBER: _ClassVar[int]
    userId: str
    oldPassword: str
    newPassword: str
    def __init__(self, userId: _Optional[str] = ..., oldPassword: _Optional[str] = ..., newPassword: _Optional[str] = ...) -> None: ...

class ChangePasswordResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ChangePasswordSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[ChangePasswordSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ChangePasswordSuccess(_message.Message):
    __slots__ = ("updated",)
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    updated: bool
    def __init__(self, updated: bool = ...) -> None: ...

class GetWalletTransactionsRequest(_message.Message):
    __slots__ = ("userId", "pagination")
    USERID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    userId: str
    pagination: PaginationRequest
    def __init__(self, userId: _Optional[str] = ..., pagination: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetWalletTransactionsResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: WalletTransactionsSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[WalletTransactionsSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class WalletTransactionsSuccess(_message.Message):
    __slots__ = ("transactions", "pagination")
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[WalletTransaction]
    pagination: PaginationResponse
    def __init__(self, transactions: _Optional[_Iterable[_Union[WalletTransaction, _Mapping]]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class GetAllUsersRequest(_message.Message):
    __slots__ = ("pagination",)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: PaginationRequest
    def __init__(self, pagination: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetAllUserEmailsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllUsersResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: AllUsersSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[AllUsersSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetAllUserEmailsResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: AllUserEmailsSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[AllUserEmailsSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class AllUserEmailsSuccess(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, email: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUsersByIdsResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UsersResponse
    error: Error
    def __init__(self, success: _Optional[_Union[UsersResponse, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class UsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserData]
    def __init__(self, users: _Optional[_Iterable[_Union[UserData, _Mapping]]] = ...) -> None: ...

class AllUsersSuccess(_message.Message):
    __slots__ = ("users", "pagination")
    USERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserData]
    pagination: PaginationResponse
    def __init__(self, users: _Optional[_Iterable[_Union[UserData, _Mapping]]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("userId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    def __init__(self, userId: _Optional[str] = ...) -> None: ...

class GetUsersByIdsRequest(_message.Message):
    __slots__ = ("userIds",)
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    userIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, userIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCurrentUserRequest(_message.Message):
    __slots__ = ("userId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    def __init__(self, userId: _Optional[str] = ...) -> None: ...

class CheckUserByEmailRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class EmailExist(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: str
    error: str
    def __init__(self, success: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class CheckUserByEmailResponse(_message.Message):
    __slots__ = ("response", "error")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    response: EmailExist
    error: Error
    def __init__(self, response: _Optional[_Union[EmailExist, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetCurrentUserResponse(_message.Message):
    __slots__ = ("user", "error")
    USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    user: UserData
    error: Error
    def __init__(self, user: _Optional[_Union[UserData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user", "error")
    USER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    user: UserData
    error: Error
    def __init__(self, user: _Optional[_Union[UserData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class BlockUserRequest(_message.Message):
    __slots__ = ("userId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    def __init__(self, userId: _Optional[str] = ...) -> None: ...

class UnBlockUserRequest(_message.Message):
    __slots__ = ("userId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userId: str
    def __init__(self, userId: _Optional[str] = ...) -> None: ...

class BlockUserResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: BlockUserSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[BlockUserSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class UnBlockUserResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UnBlockUserSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[UnBlockUserSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class BlockUserSuccess(_message.Message):
    __slots__ = ("updated",)
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    updated: bool
    def __init__(self, updated: bool = ...) -> None: ...

class UnBlockUserSuccess(_message.Message):
    __slots__ = ("updated",)
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    updated: bool
    def __init__(self, updated: bool = ...) -> None: ...

class GetAllInstructorsRequest(_message.Message):
    __slots__ = ("pagination",)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: PaginationRequest
    def __init__(self, pagination: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetAllInstructorsResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: AllInstructorsSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[AllInstructorsSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class AllInstructorsSuccess(_message.Message):
    __slots__ = ("instructors", "pagination")
    INSTRUCTORS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    instructors: _containers.RepeatedCompositeFieldContainer[UserData]
    pagination: PaginationResponse
    def __init__(self, instructors: _Optional[_Iterable[_Union[UserData, _Mapping]]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...
