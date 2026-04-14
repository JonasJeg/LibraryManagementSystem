from typing import List
from library_management_system.models.book import Book
from library_management_system.models.user import User
from library_management_system.models.borrow_record import BorrowRecord

class FileStorage:
    def __init__(self, books_file: str = "books.csv", users_file: str = "users.csv", records_file: str = "records.csv"):
        self.books_file = books_file
        self.users_file = users_file
        self.records_file = records_file

    def save_books(self, books: List[Book]) -> None:
        pass

    def load_books(self) -> List[Book]:
        pass

    def save_users(self, users: List[User]) -> None:
        pass

    def load_users(self) -> List[User]:
        pass

    def save_records(self, records: List[BorrowRecord]) -> None:
        pass

    def load_records(self, users: List[User], books: List[Book]) -> List[BorrowRecord]:
        pass
