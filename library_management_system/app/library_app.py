from library_management_system.services.file_storage import FileStorage
from library_management_system.services.library import Library
from library_management_system.services.openlibrary_client import OpenLibraryClient


class LibraryApp:
    def __init__(self, storage_override=None):
        self.storage = storage_override if storage_override else FileStorage()
        self.library = Library(self.storage)
        self.ol_client = OpenLibraryClient()

    def run(self):
        while True:
            print("\n=== Library Management System ===")
            print("1. List all books")
            print("2. Search books (local)")
            print("3. Register user")
            print("4. List users")
            print("5. Borrow book")
            print("6. Return book")
            print("7. View borrow records")
            print("8. Search & import from OpenLibrary")
            print("9. Save & exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.list_books()
            elif choice == "2":
                self.search_books_local()
            elif choice == "3":
                self.register_user()
            elif choice == "4":
                self.list_users()
            elif choice == "5":
                self.borrow_book()
            elif choice == "6":
                self.return_book()
            elif choice == "7":
                self.view_records()
            elif choice == "8":
                self.search_openlibrary_and_import()
            elif choice == "9":
                self.save_and_exit()
                break
            else:
                print("Invalid choice.")

    def list_books(self):
        books = self.library.list_books()
        if not books:
            print("No books in library.")
        else:
            for b in books:
                print(b)

    def search_books_local(self):
        keyword = input("Enter keyword (title/author): ").strip()
        results = self.library.search_books(keyword)
        if not results:
            print("No matching books found.")
        else:
            for b in results:
                print(b)

    def register_user(self):
        name = input("Enter user name: ").strip()
        user_type = input("Enter user type (Student/Teacher): ").strip()
        try:
            user = self.library.register_user(name, user_type)
            print(f"Registered user: {user}")
        except ValueError as e:
            print(e)

    def list_users(self):
        users = self.library.list_users()
        if not users:
            print("No users registered.")
        else:
            for u in users:
                print(u)

    def borrow_book(self):
        try:
            user_id = int(input("Enter user ID: ").strip())
            book_id = int(input("Enter book ID: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        record = self.library.borrow_book(user_id, book_id)
        if record:
            print(f"Borrowed successfully: {record}")

    def return_book(self):
        try:
            record_id = int(input("Enter borrow record ID: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        if self.library.return_book(record_id):
            print("Book returned successfully.")
        else:
            print("Record not found or already returned.")

    def view_records(self):
        records = self.library.list_records()
        if not records:
            print("No borrow records.")
        else:
            for r in records:
                print(r)

    def search_openlibrary_and_import(self):
        query = input("Enter search query for OpenLibrary: ").strip()
        results = self.ol_client.search_books(query, limit=5)
        if not results:
            print("No results from OpenLibrary.")
            return

        print("\nOpenLibrary results:")
        for idx, r in enumerate(results, start=1):
            year_str = str(r["year"]) if r["year"] is not None else "Unknown"
            print(f"{idx}. {r['title']} by {r['author']} ({year_str})")

        choice = input("Select a book number to import (or press Enter to cancel): ").strip()
        if not choice:
            return

        try:
            idx = int(choice)
            if not (1 <= idx <= len(results)):
                print("Invalid selection.")
                return
        except ValueError:
            print("Invalid input.")
            return

        selected = results[idx - 1]
        genre = "Imported"  # simple placeholder
        book = self.library.add_book(
            title=selected["title"],
            author=selected["author"],
            year=selected["year"],
            genre=genre
        )
        print(f"Imported book into library: {book}")

    def save_and_exit(self):
        self.library.save_all()
        print("Data saved. Goodbye!")
