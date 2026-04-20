from library_management_system.models.book import Book


def test_book_initialization():
    b = Book(1, "Title", "Author", 2020, "Fiction")
    assert b.book_id == 1
    assert b.title == "Title"
    assert b.author == "Author"
    assert b.year == 2020
    assert b.genre == "Fiction"
    assert b.is_available is True


def test_book_borrow_success():
    b = Book(1, "T", "A", None, "G")
    assert b.borrow() is True
    assert b.is_available is False


def test_book_borrow_failure():
    b = Book(1, "T", "A", None, "G", is_available=False)
    assert b.borrow() is False


def test_book_return():
    b = Book(1, "T", "A", None, "G")
    b.borrow()
    b.return_book()
    assert b.is_available is True
