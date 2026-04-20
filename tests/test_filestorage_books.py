import csv

from library_management_system.models.book import Book
from library_management_system.services.file_storage import FileStorage


def test_save_and_load_books(tmp_path):
    books_file = tmp_path / "books.csv"
    storage = FileStorage(books_file=str(books_file))

    books = [
        Book(book_id=1, title="Dune", author="Frank Herbert", year=1965, genre="Sci-Fi", is_available=True),
        Book(book_id=2, title="1984", author="George Orwell", year=None, genre="Dystopia", is_available=False),
    ]

    storage.save_books(books)
    loaded = storage.load_books()

    assert len(loaded) == 2

    b1 = loaded[0]
    assert b1.book_id == 1
    assert b1.title == "Dune"
    assert b1.author == "Frank Herbert"
    assert b1.year == 1965
    assert b1.genre == "Sci-Fi"
    assert b1.is_available is True

    b2 = loaded[1]
    assert b2.book_id == 2
    assert b2.year is None
    assert b2.is_available is False


def test_load_books_missing_file_creates_empty(tmp_path):
    books_file = tmp_path / "missing_books.csv"
    storage = FileStorage(books_file=str(books_file))

    loaded = storage.load_books()

    assert loaded == []
    assert books_file.exists()

    with open(books_file, newline="", encoding="utf-8") as f:
        header = next(csv.reader(f))
        assert header == ["id", "title", "author", "year", "genre", "is_available"]
