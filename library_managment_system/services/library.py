from typing import List, Optional

from library_management_system.models.book import Book
from library_management_system.models.borrow_record import BorrowRecord
from library_management_system.services.file_storage import FileStorage
from library_management_system.models.user import User
from library_management_system.services.user_factory import UserFactory

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
        book = Book(self._next_book_id, title, author, year, genre)
        self._books.append(book)
        self._next_book_id += 1
        return book

    def list_books(self) -> List[Book]:
        return self._books

    def search_books(self, keyword: str) -> List[Book]:
        keyword_lower = keyword.lower()
        return [
            b for b in self._books
            if keyword_lower in b.title.lower() or keyword_lower in b.author.lower()
        ]

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        for b in self._books:
            if b.book_id == book_id:
                return b
        return None

    # Users
    def register_user(self, name: str, user_type: str) -> User:
        user = UserFactory.create_user(user_type, self._next_user_id, name)
        self._users.append(user)
        self._next_user_id += 1
        return user

    def list_users(self) -> List[User]:
        return self._users

    def find_user_by_id(self, user_id: int) -> Optional[User]:
        for u in self._users:
            if u.user_id == user_id:
                return u
        return None

    def count_active_borrows_for_user(self, user: User) -> int:
        return sum(1 for r in self._records if r.user.user_id == user.user_id and r.return_date is None)

    # Borrowing
    def borrow_book(self, user_id: int, book_id: int) -> Optional[BorrowRecord]:
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)
        if not user or not book:
            print("User or book not found.")
            return None

        if not book.is_available:
            print("Book is not available.")
            return None

        active_borrows = self.count_active_borrows_for_user(user)
        if active_borrows >= user.max_books_allowed():
            print(f"{user.get_user_type()} has reached the borrowing limit.")
            return None

        if not book.borrow():
            print("Failed to borrow book.")
            return None

        record = BorrowRecord(self._next_record_id, user, book, datetime.now())
        self._records.append(record)
        self._next_record_id += 1
        return record

    def return_book(self, record_id: int) -> bool:
        for r in self._records:
            if r.record_id == record_id and r.return_date is None:
                r.book.return_book()
                r.mark_returned()
                return True
        return False

    def list_records(self) -> List[BorrowRecord]:
        return self._records

    # Saving data
    def save_all(self) -> None:
        self._storage.save_books(self._books)
        self._storage.save_users(self._users)
        self._storage.save_records(self._records)