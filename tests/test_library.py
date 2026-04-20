from library_management_system.services.library import Library
from library_management_system.services.file_storage import FileStorage

def make_lib(tmp_path):
    return Library(FileStorage(
        books_file=str(tmp_path/"b.csv"),
        users_file=str(tmp_path/"u.csv"),
        records_file=str(tmp_path/"r.csv")
    ))

def test_add_book(tmp_path):
    lib = make_lib(tmp_path)
    b = lib.add_book("T", "A", 2020, "Fiction")
    assert b.book_id == 1
    assert b.title == "T"

def test_register_user(tmp_path):
    lib = make_lib(tmp_path)
    u = lib.register_user("Jonas", "student")
    assert u.user_id == 1

def test_borrow_book_success(tmp_path):
    lib = make_lib(tmp_path)
    book = lib.add_book("T", "A", 2020, "Fiction")
    user = lib.register_user("Jonas", "student")

    record = lib.borrow_book(user.user_id, book.book_id)
    assert record is not None
    assert book.is_available is False

def test_return_book(tmp_path):
    lib = make_lib(tmp_path)
    book = lib.add_book("T", "A", 2020, "Fiction")
    user = lib.register_user("Jonas", "student")
    record = lib.borrow_book(user.user_id, book.book_id)

    assert lib.return_book(record.record_id) is True
    assert book.is_available is True
