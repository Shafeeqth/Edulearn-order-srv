

from enum import Enum


class EVENT_TOPICS(Enum):
    # Auth-related events
    AUTH_USER_CREATE = 'auth.user.create'
    AUTH_USER_REGISTER = 'auth.user.register'
    AUTH_USER_LOGIN = 'auth.user.login'
    AUTH_USER_LOGOUT = 'auth.user.logout'
  
    # User-related events
    USER_USER_UPDATED = "user.user.updated"
    USER_USER_CREATED = "user.user.created"
    USER_USER_DELETED = "user.user.deleted"
    
    USER_INSTRUCTOR_REGISTERED = "user.instructor.registered"
    

    # Order-related events
    ORDER_COURSE_CREATED = "order.course.created"
    ORDER_COURSE_UPDATED = "order.course.updated"
    ORDER_COURSE_CANCELLED = "order.course.cancelled"
    ORDER_COURSE_EXPIRED = "order.course.expired"
    ORDER_COURSE_SUCCEEDED = "order.course.succeeded"
    ORDER_COURSE_FAILED = "order.course.failed"
    ORDER_COURSE_REFUNDED = "order.course.refunded"
    ORDER_COURSE_FULFILLED = "order.course.fulfilled"

    # Payment-related events
    PAYMENT_ORDER_INITIATED = "payment.order.initiated"
    PAYMENT_ORDER_SUCCEEDED = "payment.order.succeeded"
    PAYMENT_ORDER_FAILED = "payment.order.failed"
    PAYMENT_ORDER_PENDING = "payment.order.pending"
    PAYMENT_ORDER_CANCELLED = "payment.order.cancelled"
    PAYMENT_ORDER_TIMEOUT = "payment.order.timeout"
    PAYMENT_ORDER_REFUNDED = "payment.order.refunded"
    PAYMENT_ORDER_DISPUTED = "payment.order.disputed"

    # Notification events
    NOTIFICATION_EMAIL_SENT = "notification.email.sent"
    NOTIFICATION_SMS_SENT = "notification.sms.sent"
    NOTIFICATION_INAPP_SENT = "notification.inapp.sent"

    # Session/Authentication events
    SESSION_SESSION_CREATED = "session.session.created"
    SESSION_SESSION_CANCELLED = "session.session.cancelled"
    SESSION__SESSION_EXPIRED = "session.session.expired"
    SESSION_SESSION_TERMINATED = "session.session.terminated"

    # Inventory/Course events (if relevant for orders)
    COURSE_COURSE_CREATED = "course.course.created"
    COURSE_COURSE_UPDATED = "course.course.updated"
    COURSE_PROGRESS_STARTED = "course.progress.started"
    COURSE_PROGRESS_COMPLETED = "course.progress.completed"
    COURSE_ENROLLMENT_CREATED = "course.enrollment.created"
    COURSE_ENROLLMENT_CANCELLED = "course.enrollment.cancelled"
   
    
   