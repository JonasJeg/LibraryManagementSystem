from library_management_system.models.user_types import Student, Teacher

def test_student_max_books():
    assert Student(1, "Jonas").max_books_allowed() == 3

def test_teacher_max_books():
    assert Teacher(1, "Jonas").max_books_allowed() == 5
