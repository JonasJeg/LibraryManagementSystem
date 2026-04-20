import pytest

from library_management_system.models.user_types import Student, Teacher
from library_management_system.services.user_factory import UserFactory


def test_userfactory_creates_student():
    u = UserFactory.create_user("student", 1, "Jonas")
    assert isinstance(u, Student)


def test_userfactory_creates_teacher():
    u = UserFactory.create_user("teacher", 1, "Jonas")
    assert isinstance(u, Teacher)


def test_userfactory_invalid_type():
    with pytest.raises(ValueError):
        UserFactory.create_user("alien", 1, "Jonas")
