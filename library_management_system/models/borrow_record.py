from datetime import datetime
from typing import Optional

from library_management_system.models.book import Book
from library_management_system.models.user import User


class BorrowRecord:
    def __init__(self, record_id: int, user: User, book: Book, borrow_date: datetime, return_date: Optional[datetime] = None):
        self._record_id = record_id
        self._user = user
        self._book = book
        self._borrow_date = borrow_date
        self._return_date = return_date

    @property
    def record_id(self) -> int:
        return self._record_id

    @property
    def user(self) -> User:
        return self._user

    @property
    def book(self) -> Book:
        return self._book

    @property
    def borrow_date(self) -> datetime:
        return self._borrow_date

    @property
    def return_date(self) -> Optional[datetime]:
        return self._return_date

    def mark_returned(self) -> None:
        self._return_date = datetime.now()

    def __str__(self) -> str:
        borrow_str = self._borrow_date.strftime("%Y-%m-%d")
        return_str = self._return_date.strftime("%Y-%m-%d") if self._return_date else "Not returned"
        return f"[{self._record_id}] {self._user.name} -> {self._book.title} | Borrowed: {borrow_str} | Returned: {return_str}"
