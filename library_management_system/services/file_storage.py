import csv
from datetime import datetime
from typing import List

from library_management_system.models.book import Book
from library_management_system.models.borrow_record import BorrowRecord
from library_management_system.models.user import User
from library_management_system.services.user_factory import UserFactory


class FileStorage:
    def __init__(self, books_file: str = "books.csv", users_file: str = "users.csv", records_file: str = "records.csv"):
        self.books_file = books_file
        self.users_file = users_file
        self.records_file = records_file

    # Books
    def save_books(self, books: List[Book]) -> None:
        with open(self.books_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "title", "author", "year", "genre", "is_available"])
            for b in books:
                writer.writerow([
                    b.book_id,
                    b.title,
                    b.author,
                    b.year if b.year is not None else "",
                    b.genre,
                    b.is_available
                ])

    def load_books(self) -> List[Book]:
        books = []
        try:
            with open(self.books_file, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                field_map = {name.lower(): name for name in reader.fieldnames}

                for row in reader:
                    id_str = row.get(field_map.get("id", ""), "")
                    title = row.get(field_map.get("title", ""), "Unknown")
                    author = row.get(field_map.get("author", ""), "Unknown")
                    genre = row.get(field_map.get("genre", ""), "Unknown")
                    year_str = row.get(field_map.get("year", ""), "")
                    avail_str = row.get(field_map.get("is_available", ""), "True")

                    try:
                        book_id = int(id_str)
                    except ValueError:
                        continue  # skip invalid rows

                    year = int(year_str) if year_str.isdigit() else None
                    is_available = str(avail_str).lower() == "true"

                    books.append(Book(
                        book_id=book_id,
                        title=title,
                        author=author,
                        year=year,
                        genre=genre,
                        is_available=is_available
                    ))

        except FileNotFoundError:
            with open(self.books_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "title", "author", "year", "genre", "is_available"])
            return []

        return books

    # Users
    def save_users(self, users: List[User]) -> None:
        with open(self.users_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "type"])
            for u in users:
                writer.writerow([u.user_id, u.name, u.get_user_type()])

    def load_users(self) -> List[User]:
        users = []
        try:
            with open(self.users_file, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    user_id = int(row["id"])
                    name = row["name"]
                    user_type = row["type"]
                    users.append(UserFactory.create_user(user_type, user_id, name))
        except FileNotFoundError:
            pass
        return users

    # Borrow Records
    def save_records(self, records: List[BorrowRecord]) -> None:
        with open(self.records_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["record_id", "user_id", "book_id", "borrow_date", "return_date"])
            for r in records:
                writer.writerow([
                    r.record_id,
                    r.user.user_id,
                    r.book.book_id,
                    r.borrow_date.isoformat(),
                    r.return_date.isoformat() if r.return_date else ""
                ])

    def load_records(self, users: List[User], books: List[Book]) -> List[BorrowRecord]:
        records = []
        user_map = {u.user_id: u for u in users}
        book_map = {b.book_id: b for b in books}
        try:
            with open(self.records_file, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    record_id = int(row["record_id"])
                    user_id = int(row["user_id"])
                    book_id = int(row["book_id"])
                    borrow_date = datetime.fromisoformat(row["borrow_date"])
                    return_date = datetime.fromisoformat(row["return_date"]) if row["return_date"] else None
                    user = user_map.get(user_id)
                    book = book_map.get(book_id)
                    if user and book:
                        records.append(BorrowRecord(record_id, user, book, borrow_date, return_date))
        except FileNotFoundError:
            pass
        return records
