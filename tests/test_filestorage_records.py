from datetime import datetime
from library_management_system.services.file_storage import FileStorage
from library_management_system.models.book import Book
from library_management_system.models.borrow_record import BorrowRecord
from library_management_system.services.user_factory import UserFactory

def test_save_and_load_records(tmp_path):
    records_file = tmp_path / "records.csv"
    storage = FileStorage(records_file=str(records_file))

    users = [
        UserFactory.create_user("student", 1, "Alice"),
        UserFactory.create_user("teacher", 2, "Bob"),
    ]
    books = [
        Book(10, "Dune", "Frank Herbert", 1965, "Sci-Fi", True),
        Book(20, "1984", "George Orwell", 1949, "Dystopia", True),
    ]

    borrow_date = datetime(2024, 1, 1, 12, 0)
    return_date = datetime(2024, 1, 10, 12, 0)

    records = [
        BorrowRecord(100, users[0], books[0], borrow_date, None),
        BorrowRecord(200, users[1], books[1], borrow_date, return_date),
    ]

    storage.save_records(records)
    loaded = storage.load_records(users, books)

    assert len(loaded) == 2

    r1 = loaded[0]
    assert r1.record_id == 100
    assert r1.user.user_id == 1
    assert r1.book.book_id == 10
    assert r1.return_date is None

    r2 = loaded[1]
    assert r2.record_id == 200
    assert r2.return_date == return_date


def test_load_records_missing_file_returns_empty(tmp_path):
    records_file = tmp_path / "missing_records.csv"
    storage = FileStorage(records_file=str(records_file))

    loaded = storage.load_records([], [])

    assert loaded == []

def test_load_records_missing_file_returns_empty(tmp_path):
    records_file = tmp_path / "nonexistent_records.csv"
    storage = FileStorage(records_file=str(records_file))

    loaded = storage.load_records(users=[], books=[])

    assert loaded == []
    assert not records_file.exists()
