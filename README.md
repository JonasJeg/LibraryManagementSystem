<a id="readme-top"></a>

<h1 align="center">OOP Coursework</h1>

  <p align="center">
    <h2 align="center">Library Management System</h2>
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#running-the-program">Running the Program</a></li>
        <li><a href="#running-tests">Running Tests</a></li>
        <li><a href="#using-the-program">Using the Program</a></li>
      </ul>
    </li>
    <li>
      <a href="#implementation-of-4-oop-pillars">Implementation of 4 OOP Pillars</a>
      <ul>
        <li><a href="#polymorphism">Polymorphism</a></li>
        <li><a href="#inheritance">Inheritance</a></li>
        <li><a href="#abstraction">Abstraction</a></li>
        <li><a href="#encapsulation">Encapsulation</a></li>
      </ul>
    </li>
    <li><a href="#pattern-implementation">Pattern Implementation</a></li>
    <li><a href="#aggregation">Aggregation</a></li>
    <li><a href="#composition">Composition</a></li>
    <li><a href="#reading-from-file-and-writing-to-file">Reading From File And Writing to File</a></li>
    <li>
      <a href="#results-and-conclusions">Results and Conclusions </a>
      <ul>
        <li><a href="#results">Results</a></li>
        <li><a href="#conclusions">Conclusions</a></li>
        <li><a href="#room-to-grow">Room to Grow</a></li>
      </ul>
    </li>
  </ol>
</details>



## About the Project

My goal for this project was learning more practical OOP implementations. This Library Management System lets you manage a small scale library-type environment. The program allows you to add users, search online for books to import using the "OpenLibrary" API, record users borrowing and returning books.

### Running the Program

* Right click any whitespace in the "Library Management System" folder 
* Click "Open in Terminal"
* Paste this line into the terminal:
  ```sh
  python main.py
  ```
* You will see the program interface appear

### Running tests

* Right click any whitespace in the "Library Management System" folder 
* Click "Open in Terminal"
* Paste this line into the terminal:
  ```sh
  pytest -v
  ```
* You will see the test results shown after they complete

### Using the Program

* Navigate the interface by typing the shown numbers to choose different options:
1. List all localy stored books
2. Search localy saved books by entering keywords
3. Register new user, requiring a name and user type (student - maximum 3 borrowed books or teacher - maximum 5 borrowed books)
4. List registered users
5. Specify which user is borrowing what book
6. Specify borrowed record ID to return that book
7. View the borrow record
8. Search using keywords for books online to save localy
9. Save books, users and borrow record and exit program

<p align="right">(<a href="#readme-top">back to top</a>)</p>



# Functional Requirements

## Implementation of 4 OOP Pillars

### Polymorphism

Polymorphism is used in the `user_types.py` module:
```python
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
```
Both classes have the `get_user_type` and `max_books_allowed` methods but each has a different implementation of it:
* `get_user_type`: Student returns "Student" while Teacher returns "Teacher"
* `max_books_allowed`: Student  returns "3" while Teacher returns "5"

### Inheritance

Inheritance is used in the same module, as the `Student` and `Teacher` classes inherit methods `max_books_allowed` and `get_user_type` from `User` class:
```python
class User(ABC):
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name

    @abstractmethod
    def get_user_type(self) -> str:
        pass

    @abstractmethod
    def max_books_allowed(self) -> int:
        pass
```

### Abstraction

Abstraction is used in `User` class:
```python
class User(ABC):
    @abstractmethod
    def get_user_type(self) -> str:
        pass

    @abstractmethod
    def max_books_allowed(self) -> int:
        pass
```
These abstract methods require the child classes to implement them in some way.

### Encapsulation

Encapsulation is used in `User` class:
```python
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
```
This class has protected `_user_id` and `_name`, each having it's own getters, which allows these arguments to be used in child classes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Pattern Implementation

I chose the Factory Pattern and implemented it as `UserFactory` because it allowed to add different types of users without writing many `if/elseif` statements.

```python
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
```
Using this pattern allows centralizing the different user options and choosing correct code or class for each.

## Aggregation

Used in `Library` class:
```python
class Library:
    def __init__(self, storage: FileStorage):
        self._books: List[Book] = storage.load_books()
        self._users: List[User] = storage.load_users()
        self._records: List[BorrowRecord] = storage.load_records(self._users, self._books)
```
`Books`, `Users`, and the `BorrowRecords` are created indipendantly because they come from files, so deleting a created `Library` object does not delete `Books`, `Users`, and `BorrowRecords`.

## Composition

Used in `LibraryApp` class:
```python
class LibraryApp:
    def __init__(self, storage_override=None):
        self.storage = storage_override if storage_override else FileStorage()
        self.library = Library(self.storage)
        self.ol_client = OpenLibraryClient()
```
This class creates it's own `Library` class and if the `LibraryApp` object is deleted `Library` goes with it.

(If there is no `storage_override` then `self.storage` counts as composition, otherwise it is aggregation because `storage_override` is made in `main.py` file.)

## Reading From File And Writing to File

I chose to implement the `.csv` file format for storage because it is quite widely used and has a built-in module in python to make using the format much easier. The program stores books, users and the borrow record in `Library Management System\library_management_system\data`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Results and Conclusions 

## Results

* Created a good start to a project that still has room to grow
* At first I tried to use `GoogleBooks` API and realised there was a limit for the amount of requests that could be made. After consulting CopilotAI it suggested I use the `OpenLibrary` API, which has no request limit but does not have as extensive of a library as `GoogleBooks`
* The program successfully searches for books with `OpenLibrary` API using keywords and returns results, during my use of the program it has not failed.
* Had trouble with import path issues, had to make use of AI for help with understanding problems. These pathing issues were later resolved.


## Conclusions

With this coursework I learned how to make a useful python project in seperate files (modules), how to troubleshoot pathing issues and import classes from other files, how to write unit tests. Made use of GitHub to upload and save project progress. This program can be used in real applications but for it to be actualy useful it needs to be improved and new features have to be added.

## Room to Grow

* Add GUI for easier use
* Could add database integration instead of files for easier data management
* Add late return fee to discourage keeping books for too long

<p align="right">(<a href="#readme-top">back to top</a>)</p>