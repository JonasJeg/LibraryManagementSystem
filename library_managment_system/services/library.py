from typing import List, Optional

from library_management_system.models.book import Book
from library_management_system.models.borrow_record import BorrowRecord
from library_management_system.services.file_storage import FileStorage
from library_management_system.models.user import User

class Library:
    def __init__(self, storage: FileStorage):
        self._storage = storage
        self._books: List[Book] = storage.load_books()
        self._users: List[User] = storage.load_users()
        self._records: List[BorrowRecord] = storage.load_records(self._users, self._books)
        self._next_book_id = (max((b.book_id for b in self._books), default=0) + 1)
        self._next_user_id = (max((u.user_id for u in self._users), default=0) + 1)
        self._next_record_id = (max((r.record_id for r in self._records), default=0) + 1)

    # Books
    def add_book(self, title: str, author: str, year: Optional[int], genre: str) -> Book:
        pass

    def list_books(self) -> List[Book]:
        return self._books

    def search_books(self, keyword: str) -> List[Book]:
        pass
    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        pass

    # Users
    def register_user(self, name: str, user_type: str) -> User:
        pass

    def list_users(self) -> List[User]:
        return self._users

    def find_user_by_id(self, user_id: int) -> Optional[User]:
        pass

    def count_active_borrows_for_user(self, user: User) -> int:
        pass

    # Borrowing
    def borrow_book(self, user_id: int, book_id: int) -> Optional[BorrowRecord]:
        pass

    def return_book(self, record_id: int) -> bool:
        pass

    def list_records(self) -> List[BorrowRecord]:
        return self._records

    # Saving
    def save_all(self) -> None:
        pass