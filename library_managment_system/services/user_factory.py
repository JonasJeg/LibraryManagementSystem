from library_management_system.models.user_types import Student, Teacher
from library_management_system.models.user import User

class UserFactory:
    @staticmethod
    def create_user(user_type: str, user_id: int, name: str) -> User:
        user_type = user_type.lower()
        if user_type == "student":
            return Student(user_id, name)
        elif user_type == "teacher":
            return Teacher(user_id, name)
        else:
            raise ValueError(f"Unknown user type: {user_type}")
