from library_management_system.app.library_app import LibraryApp
from library_management_system.services.file_storage import FileStorage

if __name__ == "__main__":
    storage = FileStorage(
        books_file="library_management_system/data/books.csv",
        users_file="library_management_system/data/users.csv",
        records_file="library_management_system/data/records.csv"
    )

    app = LibraryApp(storage_override=storage)
    app.run()