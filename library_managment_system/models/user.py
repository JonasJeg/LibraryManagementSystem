from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def get_user_type(self) -> str:
        pass

    @abstractmethod
    def max_books_allowed(self) -> int:
        pass

    def __str__(self) -> str:
        return f"[{self._user_id}] {self._name} ({self.get_user_type()})"
