from .user import User


class Student(User):
    def get_user_type(self) -> str:
        return "Student"

    def max_books_allowed(self) -> int:
        return 3


class Teacher(User):
    def get_user_type(self) -> str:
        return "Teacher"

    def max_books_allowed(self) -> int:
        return 5
