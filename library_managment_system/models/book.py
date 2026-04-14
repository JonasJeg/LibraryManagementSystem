from typing import Optional

class Book:
    def __init__(self, book_id: int, title: str, author: str, year: Optional[int], genre: str, is_available: bool = True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre
        self._is_available = is_available

    @property
    def book_id(self) -> int:
        return self._book_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> Optional[int]:
        return self._year

    @property
    def genre(self) -> str:
        return self._genre

    @property
    def is_available(self) -> bool:
        return self._is_available

    def borrow(self) -> bool:
        pass

    def return_book(self) -> None:
        pass

    def __str__(self) -> str:
        pass