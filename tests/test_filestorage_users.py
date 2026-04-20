from library_management_system.services.file_storage import FileStorage
from library_management_system.services.user_factory import UserFactory

def test_save_and_load_users(tmp_path):
    users_file = tmp_path / "users.csv"
    storage = FileStorage(users_file=str(users_file))

    users = [
        UserFactory.create_user("student", 1, "Alice"),
        UserFactory.create_user("teacher", 2, "Bob"),
    ]

    storage.save_users(users)
    loaded = storage.load_users()

    assert len(loaded) == 2

    u1 = loaded[0]
    assert u1.user_id == 1
    assert u1.name == "Alice"
    assert u1.get_user_type() == "Student"

    u2 = loaded[1]
    assert u2.user_id == 2
    assert u2.name == "Bob"
    assert u2.get_user_type() == "Teacher"


def test_load_users_missing_file_returns_empty(tmp_path):
    users_file = tmp_path / "missing_users.csv"
    storage = FileStorage(users_file=str(users_file))

    loaded = storage.load_users()

    assert loaded == []

def test_load_users_missing_file_returns_empty(tmp_path):
    users_file = tmp_path / "nonexistent_users.csv"
    storage = FileStorage(users_file=str(users_file))

    loaded = storage.load_users()

    assert loaded == []
    assert not users_file.exists()
