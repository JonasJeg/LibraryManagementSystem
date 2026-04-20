from datetime import datetime

from library_management_system.models.book import Book
from library_management_system.models.borrow_record import BorrowRecord
from library_management_system.models.user_types import Student


def test_borrowrecord_initialization():
    user = Student(1, "Jonas")
    book = Book(1, "T", "A", None, "G")
    now = datetime.now()

    r = BorrowRecord(1, user, book, now)
    assert r.record_id == 1
    assert r.user == user
    assert r.book == book
    assert r.borrow_date == now
    assert r.return_date is None


def test_borrowrecord_mark_returned():
    user = Student(1, "Jonas")
    book = Book(1, "T", "A", None, "G")
    r = BorrowRecord(1, user, book, datetime.now())

    r.mark_returned()
    assert r.return_date is not None
