from src.domain.entities.session_booking import SessionBooking
from src.domain.value_objects.money import Money
from datetime import datetime

def test_session_booking_creation():
    booking = SessionBooking.create(user_id="user1", session_id="session1", amount=Money(50.0))
    assert booking.id is not None
    assert booking.user_id == "user1"
    assert booking.session_id == "session1"
    assert booking.amount.amount == 50.0
    assert booking.status == "PENDING"
    assert booking.version == 1
    assert isinstance(booking.created_at, datetime)

def test_session_booking_confirm():
    booking = SessionBooking.create(user_id="user1", session_id="session1", amount=Money(50.0))
    original_updated_at = booking.updated_at
    booking.confirm()
    assert booking.status == "CONFIRMED"
    assert booking.version == 2
    assert booking.updated_at > original_updated_at

def test_session_booking_cancel():
    booking = SessionBooking.create(user_id="user1", session_id="session1", amount=Money(50.0))
    original_updated_at = booking.updated_at
    booking.cancel()
    assert booking.status == "CANCELLED"
    assert booking.version == 2
    assert booking.updated_at > original_updated_at