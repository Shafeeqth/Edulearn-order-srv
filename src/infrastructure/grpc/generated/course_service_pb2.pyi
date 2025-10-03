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

class Pagination(_message.Message):
    __slots__ = ("page", "limit", "sort_by", "sort_order")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    sort_by: str
    sort_order: str
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ..., sort_by: _Optional[str] = ..., sort_order: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "name", "avatar", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    avatar: str
    email: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., avatar: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class CreateCourseRequest(_message.Message):
    __slots__ = ("title", "topics", "instructor_id", "instructor", "sub_title", "category", "sub_category", "language", "level", "subtitle_language", "duration_value", "duration_unit")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    DURATION_UNIT_FIELD_NUMBER: _ClassVar[int]
    title: str
    topics: _containers.RepeatedScalarFieldContainer[str]
    instructor_id: str
    instructor: User
    sub_title: str
    category: str
    sub_category: str
    language: str
    level: str
    subtitle_language: str
    duration_value: str
    duration_unit: str
    def __init__(self, title: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., instructor_id: _Optional[str] = ..., instructor: _Optional[_Union[User, _Mapping]] = ..., sub_title: _Optional[str] = ..., category: _Optional[str] = ..., sub_category: _Optional[str] = ..., language: _Optional[str] = ..., level: _Optional[str] = ..., subtitle_language: _Optional[str] = ..., duration_value: _Optional[str] = ..., duration_unit: _Optional[str] = ...) -> None: ...

class GetCourseRequest(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class GetCoursesByIdsRequest(_message.Message):
    __slots__ = ("course_ids",)
    COURSE_IDS_FIELD_NUMBER: _ClassVar[int]
    course_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, course_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCoursesByIdsResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CoursesResponse
    error: Error
    def __init__(self, success: _Optional[_Union[CoursesResponse, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetCourseBySlugRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetAllCoursesRequest(_message.Message):
    __slots__ = ("pagination",)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: Pagination
    def __init__(self, pagination: _Optional[_Union[Pagination, _Mapping]] = ...) -> None: ...

class UpdateCourseRequest(_message.Message):
    __slots__ = ("title", "topics", "sub_title", "category", "sub_category", "language", "level", "subtitle_language", "duration_value", "duration_unit", "course_id", "description", "learning_outcomes", "target_audience", "requirements", "thumbnail", "trailer", "price", "discount_price", "currency")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    DURATION_UNIT_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEARNING_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    TRAILER_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    title: str
    topics: _containers.RepeatedScalarFieldContainer[str]
    sub_title: str
    category: str
    sub_category: str
    language: str
    level: str
    subtitle_language: str
    duration_value: str
    duration_unit: str
    course_id: str
    description: str
    learning_outcomes: _containers.RepeatedScalarFieldContainer[str]
    target_audience: _containers.RepeatedScalarFieldContainer[str]
    requirements: _containers.RepeatedScalarFieldContainer[str]
    thumbnail: str
    trailer: str
    price: int
    discount_price: int
    currency: str
    def __init__(self, title: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., sub_title: _Optional[str] = ..., category: _Optional[str] = ..., sub_category: _Optional[str] = ..., language: _Optional[str] = ..., level: _Optional[str] = ..., subtitle_language: _Optional[str] = ..., duration_value: _Optional[str] = ..., duration_unit: _Optional[str] = ..., course_id: _Optional[str] = ..., description: _Optional[str] = ..., learning_outcomes: _Optional[_Iterable[str]] = ..., target_audience: _Optional[_Iterable[str]] = ..., requirements: _Optional[_Iterable[str]] = ..., thumbnail: _Optional[str] = ..., trailer: _Optional[str] = ..., price: _Optional[int] = ..., discount_price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class DeleteCourseRequest(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class GetCoursesByInstructorRequest(_message.Message):
    __slots__ = ("instructor_id", "pagination")
    INSTRUCTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    instructor_id: str
    pagination: Pagination
    def __init__(self, instructor_id: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ...) -> None: ...

class GetEnrolledCoursesRequest(_message.Message):
    __slots__ = ("user_id", "pagination")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pagination: Pagination
    def __init__(self, user_id: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ...) -> None: ...

class CourseData(_message.Message):
    __slots__ = ("id", "title", "topics", "instructor_id", "sub_title", "category", "sub_category", "language", "subtitle_language", "level", "duration_value", "duration_unit", "description", "learning_outcomes", "target_audience", "requirements", "thumbnail", "trailer", "status", "slug", "rating", "numberOfRating", "enrollments", "sections", "created_at", "updated_at", "deleted_at", "price", "discount_price", "currency", "instructor")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    DURATION_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEARNING_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    TRAILER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFRATING_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENTS_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    topics: _containers.RepeatedScalarFieldContainer[str]
    instructor_id: str
    sub_title: str
    category: str
    sub_category: str
    language: str
    subtitle_language: str
    level: str
    duration_value: str
    duration_unit: str
    description: str
    learning_outcomes: _containers.RepeatedScalarFieldContainer[str]
    target_audience: _containers.RepeatedScalarFieldContainer[str]
    requirements: _containers.RepeatedScalarFieldContainer[str]
    thumbnail: str
    trailer: str
    status: str
    slug: str
    rating: int
    numberOfRating: int
    enrollments: int
    sections: _containers.RepeatedCompositeFieldContainer[SectionData]
    created_at: str
    updated_at: str
    deleted_at: str
    price: int
    discount_price: int
    currency: str
    instructor: User
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., instructor_id: _Optional[str] = ..., sub_title: _Optional[str] = ..., category: _Optional[str] = ..., sub_category: _Optional[str] = ..., language: _Optional[str] = ..., subtitle_language: _Optional[str] = ..., level: _Optional[str] = ..., duration_value: _Optional[str] = ..., duration_unit: _Optional[str] = ..., description: _Optional[str] = ..., learning_outcomes: _Optional[_Iterable[str]] = ..., target_audience: _Optional[_Iterable[str]] = ..., requirements: _Optional[_Iterable[str]] = ..., thumbnail: _Optional[str] = ..., trailer: _Optional[str] = ..., status: _Optional[str] = ..., slug: _Optional[str] = ..., rating: _Optional[int] = ..., numberOfRating: _Optional[int] = ..., enrollments: _Optional[int] = ..., sections: _Optional[_Iterable[_Union[SectionData, _Mapping]]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., deleted_at: _Optional[str] = ..., price: _Optional[int] = ..., discount_price: _Optional[int] = ..., currency: _Optional[str] = ..., instructor: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CourseResponse(_message.Message):
    __slots__ = ("course", "error")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    course: CourseData
    error: Error
    def __init__(self, course: _Optional[_Union[CourseData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class CoursesData(_message.Message):
    __slots__ = ("courses", "total")
    COURSES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    courses: _containers.RepeatedCompositeFieldContainer[CourseData]
    total: int
    def __init__(self, courses: _Optional[_Iterable[_Union[CourseData, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class CoursesResponse(_message.Message):
    __slots__ = ("courses", "error")
    COURSES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    courses: CoursesData
    error: Error
    def __init__(self, courses: _Optional[_Union[CoursesData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteCourseResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteSuccess(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class CreateSectionRequest(_message.Message):
    __slots__ = ("course_id", "title", "description", "order", "is_published")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    title: str
    description: str
    order: int
    is_published: bool
    def __init__(self, course_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., order: _Optional[int] = ..., is_published: bool = ...) -> None: ...

class GetSectionRequest(_message.Message):
    __slots__ = ("section_id",)
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    section_id: str
    def __init__(self, section_id: _Optional[str] = ...) -> None: ...

class UpdateSectionRequest(_message.Message):
    __slots__ = ("section_id", "title", "description", "is_published", "order")
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    section_id: str
    title: str
    description: str
    is_published: bool
    order: int
    def __init__(self, section_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., is_published: bool = ..., order: _Optional[int] = ...) -> None: ...

class DeleteSectionRequest(_message.Message):
    __slots__ = ("section_id",)
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    section_id: str
    def __init__(self, section_id: _Optional[str] = ...) -> None: ...

class GetSectionsByCourseRequest(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class SectionData(_message.Message):
    __slots__ = ("id", "course_id", "title", "lessons", "created_at", "updated_at", "deleted_at", "description", "is_published", "order", "quiz")
    ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LESSONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    QUIZ_FIELD_NUMBER: _ClassVar[int]
    id: str
    course_id: str
    title: str
    lessons: _containers.RepeatedCompositeFieldContainer[LessonData]
    created_at: str
    updated_at: str
    deleted_at: str
    description: str
    is_published: bool
    order: int
    quiz: QuizData
    def __init__(self, id: _Optional[str] = ..., course_id: _Optional[str] = ..., title: _Optional[str] = ..., lessons: _Optional[_Iterable[_Union[LessonData, _Mapping]]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., deleted_at: _Optional[str] = ..., description: _Optional[str] = ..., is_published: bool = ..., order: _Optional[int] = ..., quiz: _Optional[_Union[QuizData, _Mapping]] = ...) -> None: ...

class SectionResponse(_message.Message):
    __slots__ = ("section", "error")
    SECTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    section: SectionData
    error: Error
    def __init__(self, section: _Optional[_Union[SectionData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class SectionsData(_message.Message):
    __slots__ = ("sections",)
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    sections: _containers.RepeatedCompositeFieldContainer[SectionData]
    def __init__(self, sections: _Optional[_Iterable[_Union[SectionData, _Mapping]]] = ...) -> None: ...

class SectionsResponse(_message.Message):
    __slots__ = ("sections", "error")
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sections: SectionsData
    error: Error
    def __init__(self, sections: _Optional[_Union[SectionsData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteSectionResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class CreateLessonRequest(_message.Message):
    __slots__ = ("section_id", "course_id", "is_preview", "description", "estimated_duration", "order", "title", "is_published", "content_type", "content_url", "metadata")
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    section_id: str
    course_id: str
    is_preview: bool
    description: str
    estimated_duration: int
    order: int
    title: str
    is_published: bool
    content_type: str
    content_url: str
    metadata: ContentMetaData
    def __init__(self, section_id: _Optional[str] = ..., course_id: _Optional[str] = ..., is_preview: bool = ..., description: _Optional[str] = ..., estimated_duration: _Optional[int] = ..., order: _Optional[int] = ..., title: _Optional[str] = ..., is_published: bool = ..., content_type: _Optional[str] = ..., content_url: _Optional[str] = ..., metadata: _Optional[_Union[ContentMetaData, _Mapping]] = ...) -> None: ...

class GetLessonRequest(_message.Message):
    __slots__ = ("lesson_id", "courseId")
    LESSON_ID_FIELD_NUMBER: _ClassVar[int]
    COURSEID_FIELD_NUMBER: _ClassVar[int]
    lesson_id: str
    courseId: str
    def __init__(self, lesson_id: _Optional[str] = ..., courseId: _Optional[str] = ...) -> None: ...

class UpdateLessonRequest(_message.Message):
    __slots__ = ("lesson_id", "section_id", "is_preview", "description", "estimated_duration", "order", "title", "is_published", "content_type", "content_url", "metadata")
    LESSON_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    lesson_id: str
    section_id: str
    is_preview: bool
    description: str
    estimated_duration: int
    order: int
    title: str
    is_published: bool
    content_type: str
    content_url: str
    metadata: ContentMetaData
    def __init__(self, lesson_id: _Optional[str] = ..., section_id: _Optional[str] = ..., is_preview: bool = ..., description: _Optional[str] = ..., estimated_duration: _Optional[int] = ..., order: _Optional[int] = ..., title: _Optional[str] = ..., is_published: bool = ..., content_type: _Optional[str] = ..., content_url: _Optional[str] = ..., metadata: _Optional[_Union[ContentMetaData, _Mapping]] = ...) -> None: ...

class ContentMetaData(_message.Message):
    __slots__ = ("title", "file_name", "mime_type", "file_size", "url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    file_name: str
    mime_type: str
    file_size: str
    url: str
    def __init__(self, title: _Optional[str] = ..., file_name: _Optional[str] = ..., mime_type: _Optional[str] = ..., file_size: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class DeleteLessonRequest(_message.Message):
    __slots__ = ("lesson_id",)
    LESSON_ID_FIELD_NUMBER: _ClassVar[int]
    lesson_id: str
    def __init__(self, lesson_id: _Optional[str] = ...) -> None: ...

class GetLessonsBySectionRequest(_message.Message):
    __slots__ = ("section_id",)
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    section_id: str
    def __init__(self, section_id: _Optional[str] = ...) -> None: ...

class LessonData(_message.Message):
    __slots__ = ("id", "section_id", "is_preview", "description", "estimated_duration", "order", "title", "is_published", "content_type", "content_url", "metadata", "created_at", "updated_at", "deleted_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    section_id: str
    is_preview: bool
    description: str
    estimated_duration: int
    order: int
    title: str
    is_published: bool
    content_type: str
    content_url: str
    metadata: ContentMetaData
    created_at: str
    updated_at: str
    deleted_at: str
    def __init__(self, id: _Optional[str] = ..., section_id: _Optional[str] = ..., is_preview: bool = ..., description: _Optional[str] = ..., estimated_duration: _Optional[int] = ..., order: _Optional[int] = ..., title: _Optional[str] = ..., is_published: bool = ..., content_type: _Optional[str] = ..., content_url: _Optional[str] = ..., metadata: _Optional[_Union[ContentMetaData, _Mapping]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., deleted_at: _Optional[str] = ...) -> None: ...

class LessonResponse(_message.Message):
    __slots__ = ("lesson", "error")
    LESSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    lesson: LessonData
    error: Error
    def __init__(self, lesson: _Optional[_Union[LessonData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class LessonsData(_message.Message):
    __slots__ = ("lessons",)
    LESSONS_FIELD_NUMBER: _ClassVar[int]
    lessons: _containers.RepeatedCompositeFieldContainer[LessonData]
    def __init__(self, lessons: _Optional[_Iterable[_Union[LessonData, _Mapping]]] = ...) -> None: ...

class LessonsResponse(_message.Message):
    __slots__ = ("lessons", "error")
    LESSONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    lessons: LessonsData
    error: Error
    def __init__(self, lessons: _Optional[_Union[LessonsData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteLessonResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class Question(_message.Message):
    __slots__ = ("id", "type", "points", "time_limit", "question", "required", "options", "correct_answer", "explanation")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CORRECT_ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    points: int
    time_limit: int
    question: str
    required: bool
    options: _containers.RepeatedScalarFieldContainer[str]
    correct_answer: str
    explanation: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., points: _Optional[int] = ..., time_limit: _Optional[int] = ..., question: _Optional[str] = ..., required: bool = ..., options: _Optional[_Iterable[str]] = ..., correct_answer: _Optional[str] = ..., explanation: _Optional[str] = ...) -> None: ...

class CreateQuizRequest(_message.Message):
    __slots__ = ("course_id", "section_id", "description", "title", "isRequired", "time_limit", "passing_score", "max_attempts", "questions")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ISREQUIRED_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PASSING_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    section_id: str
    description: str
    title: str
    isRequired: bool
    time_limit: int
    passing_score: int
    max_attempts: int
    questions: _containers.RepeatedCompositeFieldContainer[Question]
    def __init__(self, course_id: _Optional[str] = ..., section_id: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., isRequired: bool = ..., time_limit: _Optional[int] = ..., passing_score: _Optional[int] = ..., max_attempts: _Optional[int] = ..., questions: _Optional[_Iterable[_Union[Question, _Mapping]]] = ...) -> None: ...

class GetQuizRequest(_message.Message):
    __slots__ = ("quiz_id",)
    QUIZ_ID_FIELD_NUMBER: _ClassVar[int]
    quiz_id: str
    def __init__(self, quiz_id: _Optional[str] = ...) -> None: ...

class UpdateQuizRequest(_message.Message):
    __slots__ = ("quiz_id", "description", "title", "isRequired", "time_limit", "passing_score", "max_attempts", "questions")
    QUIZ_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ISREQUIRED_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PASSING_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    quiz_id: str
    description: str
    title: str
    isRequired: bool
    time_limit: int
    passing_score: int
    max_attempts: int
    questions: _containers.RepeatedCompositeFieldContainer[Question]
    def __init__(self, quiz_id: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., isRequired: bool = ..., time_limit: _Optional[int] = ..., passing_score: _Optional[int] = ..., max_attempts: _Optional[int] = ..., questions: _Optional[_Iterable[_Union[Question, _Mapping]]] = ...) -> None: ...

class DeleteQuizRequest(_message.Message):
    __slots__ = ("quiz_id",)
    QUIZ_ID_FIELD_NUMBER: _ClassVar[int]
    quiz_id: str
    def __init__(self, quiz_id: _Optional[str] = ...) -> None: ...

class GetQuizzesByCourseRequest(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class QuizData(_message.Message):
    __slots__ = ("id", "course_id", "section_id", "title", "description", "time_limit", "passing_score", "questions", "created_at", "updated_at", "deleted_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PASSING_SCORE_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    course_id: str
    section_id: str
    title: str
    description: str
    time_limit: int
    passing_score: int
    questions: _containers.RepeatedCompositeFieldContainer[Question]
    created_at: str
    updated_at: str
    deleted_at: str
    def __init__(self, id: _Optional[str] = ..., course_id: _Optional[str] = ..., section_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., time_limit: _Optional[int] = ..., passing_score: _Optional[int] = ..., questions: _Optional[_Iterable[_Union[Question, _Mapping]]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., deleted_at: _Optional[str] = ...) -> None: ...

class QuizResponse(_message.Message):
    __slots__ = ("quiz", "error")
    QUIZ_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    quiz: QuizData
    error: Error
    def __init__(self, quiz: _Optional[_Union[QuizData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class QuizzesData(_message.Message):
    __slots__ = ("quizzes",)
    QUIZZES_FIELD_NUMBER: _ClassVar[int]
    quizzes: _containers.RepeatedCompositeFieldContainer[QuizData]
    def __init__(self, quizzes: _Optional[_Iterable[_Union[QuizData, _Mapping]]] = ...) -> None: ...

class QuizzesResponse(_message.Message):
    __slots__ = ("quizzes", "error")
    QUIZZES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    quizzes: QuizzesData
    error: Error
    def __init__(self, quizzes: _Optional[_Union[QuizzesData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteQuizResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class CreateEnrollmentRequest(_message.Message):
    __slots__ = ("user_id", "course_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    course_id: str
    def __init__(self, user_id: _Optional[str] = ..., course_id: _Optional[str] = ...) -> None: ...

class GetEnrollmentRequest(_message.Message):
    __slots__ = ("enrollment_id",)
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    def __init__(self, enrollment_id: _Optional[str] = ...) -> None: ...

class UpdateEnrollmentRequest(_message.Message):
    __slots__ = ("enrollment_id", "status")
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    status: str
    def __init__(self, enrollment_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DeleteEnrollmentRequest(_message.Message):
    __slots__ = ("enrollment_id",)
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    def __init__(self, enrollment_id: _Optional[str] = ...) -> None: ...

class GetEnrollmentsByUserRequest(_message.Message):
    __slots__ = ("user_id", "pagination")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    pagination: Pagination
    def __init__(self, user_id: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ...) -> None: ...

class GetEnrollmentsByCourseRequest(_message.Message):
    __slots__ = ("course_id", "pagination")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    pagination: Pagination
    def __init__(self, course_id: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ...) -> None: ...

class EnrollmentData(_message.Message):
    __slots__ = ("id", "user_id", "course_id", "status", "progress", "enrolled_at", "completed_at", "created_at", "updated_at", "deleted_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ENROLLED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    course_id: str
    status: str
    progress: float
    enrolled_at: str
    completed_at: str
    created_at: str
    updated_at: str
    deleted_at: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., course_id: _Optional[str] = ..., status: _Optional[str] = ..., progress: _Optional[float] = ..., enrolled_at: _Optional[str] = ..., completed_at: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., deleted_at: _Optional[str] = ...) -> None: ...

class EnrollmentResponse(_message.Message):
    __slots__ = ("enrollment", "error")
    ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    enrollment: EnrollmentData
    error: Error
    def __init__(self, enrollment: _Optional[_Union[EnrollmentData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class EnrollmentsData(_message.Message):
    __slots__ = ("enrollments",)
    ENROLLMENTS_FIELD_NUMBER: _ClassVar[int]
    enrollments: _containers.RepeatedCompositeFieldContainer[EnrollmentData]
    def __init__(self, enrollments: _Optional[_Iterable[_Union[EnrollmentData, _Mapping]]] = ...) -> None: ...

class EnrollmentsResponse(_message.Message):
    __slots__ = ("enrollments", "error")
    ENROLLMENTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    enrollments: EnrollmentsData
    error: Error
    def __init__(self, enrollments: _Optional[_Union[EnrollmentsData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteEnrollmentResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class CreateProgressRequest(_message.Message):
    __slots__ = ("enrollment_id", "lesson_id", "progress")
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LESSON_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    lesson_id: str
    progress: float
    def __init__(self, enrollment_id: _Optional[str] = ..., lesson_id: _Optional[str] = ..., progress: _Optional[float] = ...) -> None: ...

class GetProgressRequest(_message.Message):
    __slots__ = ("progress_id",)
    PROGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    progress_id: str
    def __init__(self, progress_id: _Optional[str] = ...) -> None: ...

class UpdateProgressRequest(_message.Message):
    __slots__ = ("progress_id", "progress", "completed")
    PROGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    progress_id: str
    progress: float
    completed: bool
    def __init__(self, progress_id: _Optional[str] = ..., progress: _Optional[float] = ..., completed: bool = ...) -> None: ...

class DeleteProgressRequest(_message.Message):
    __slots__ = ("progress_id",)
    PROGRESS_ID_FIELD_NUMBER: _ClassVar[int]
    progress_id: str
    def __init__(self, progress_id: _Optional[str] = ...) -> None: ...

class GetProgressByEnrollmentRequest(_message.Message):
    __slots__ = ("enrollment_id",)
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    def __init__(self, enrollment_id: _Optional[str] = ...) -> None: ...

class ProgressData(_message.Message):
    __slots__ = ("id", "enrollment_id", "lesson_id", "deleted_at", "completed", "completed_at", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LESSON_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    enrollment_id: str
    lesson_id: str
    deleted_at: str
    completed: bool
    completed_at: str
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., enrollment_id: _Optional[str] = ..., lesson_id: _Optional[str] = ..., deleted_at: _Optional[str] = ..., completed: bool = ..., completed_at: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class ProgressResponse(_message.Message):
    __slots__ = ("progress", "error")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    progress: ProgressData
    error: Error
    def __init__(self, progress: _Optional[_Union[ProgressData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ProgressesData(_message.Message):
    __slots__ = ("progresses",)
    PROGRESSES_FIELD_NUMBER: _ClassVar[int]
    progresses: _containers.RepeatedCompositeFieldContainer[ProgressData]
    def __init__(self, progresses: _Optional[_Iterable[_Union[ProgressData, _Mapping]]] = ...) -> None: ...

class ProgressesResponse(_message.Message):
    __slots__ = ("progresses", "error")
    PROGRESSES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    progresses: ProgressesData
    error: Error
    def __init__(self, progresses: _Optional[_Union[ProgressesData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteProgressResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class CreateReviewRequest(_message.Message):
    __slots__ = ("user_id", "course_id", "rating", "comment")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    course_id: str
    rating: int
    comment: str
    def __init__(self, user_id: _Optional[str] = ..., course_id: _Optional[str] = ..., rating: _Optional[int] = ..., comment: _Optional[str] = ...) -> None: ...

class GetReviewRequest(_message.Message):
    __slots__ = ("review_id",)
    REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    review_id: str
    def __init__(self, review_id: _Optional[str] = ...) -> None: ...

class UpdateReviewRequest(_message.Message):
    __slots__ = ("review_id", "rating", "comment")
    REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    review_id: str
    rating: int
    comment: str
    def __init__(self, review_id: _Optional[str] = ..., rating: _Optional[int] = ..., comment: _Optional[str] = ...) -> None: ...

class DeleteReviewRequest(_message.Message):
    __slots__ = ("review_id",)
    REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    review_id: str
    def __init__(self, review_id: _Optional[str] = ...) -> None: ...

class GetReviewsByCourseRequest(_message.Message):
    __slots__ = ("course_id", "pagination")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    pagination: Pagination
    def __init__(self, course_id: _Optional[str] = ..., pagination: _Optional[_Union[Pagination, _Mapping]] = ...) -> None: ...

class ReviewData(_message.Message):
    __slots__ = ("id", "user_id", "course_id", "rating", "comment", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    course_id: str
    rating: int
    comment: str
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., course_id: _Optional[str] = ..., rating: _Optional[int] = ..., comment: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class ReviewResponse(_message.Message):
    __slots__ = ("review", "error")
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    review: ReviewData
    error: Error
    def __init__(self, review: _Optional[_Union[ReviewData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ReviewsData(_message.Message):
    __slots__ = ("reviews",)
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    reviews: _containers.RepeatedCompositeFieldContainer[ReviewData]
    def __init__(self, reviews: _Optional[_Iterable[_Union[ReviewData, _Mapping]]] = ...) -> None: ...

class ReviewsResponse(_message.Message):
    __slots__ = ("reviews", "error")
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    reviews: ReviewsData
    error: Error
    def __init__(self, reviews: _Optional[_Union[ReviewsData, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class DeleteReviewResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    error: Error
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
