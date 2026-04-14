from library_management_system.services.file_storage import FileStorage
from library_management_system.services.library import Library

class LibraryApp:
    def __init__(self):
        self.storage = FileStorage()
        self.library = Library(self.storage)
        self.ol_client = OpenLibraryClient()

    def run(self):
        pass

    def list_books(self):
        pass

    def search_books_local(self):
        pass

    def register_user(self):
        pass

    def list_users(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def view_records(self):
        pass

    def save_and_exit(self):
        pass