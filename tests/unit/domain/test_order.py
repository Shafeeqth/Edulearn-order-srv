from src.domain.entities.order import Order
from src.domain.value_objects.money import Money
from datetime import datetime

def test_order_creation():
    order = Order.create(user_id="user1", course_ids=["course1", "course2"], total_amount=Money(200.0))
    assert order.id is not None
    assert order.user_id == "user1"
    assert order.course_ids == ["course1", "course2"]
    assert order.total_amount.amount == 200.0
    assert order.status == "PENDING"
    assert isinstance(order.created_at, datetime)

def test_order_mark_completed():
    order = Order.create(user_id="user1", course_ids=["course1"], total_amount=Money(100.0))
    original_updated_at = order.updated_at
    order.mark_completed()
    assert order.status == "COMPLETED"
    assert order.updated_at > original_updated_at

def test_order_mark_failed():
    order = Order.create(user_id="user1", course_ids=["course1"], total_amount=Money(100.0))
    original_updated_at = order.updated_at
    order.mark_failed()
    assert order.status == "FAILED"
    assert order.updated_at > original_updated_at