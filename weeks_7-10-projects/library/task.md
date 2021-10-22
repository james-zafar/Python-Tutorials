In this project you will attempt to build a UI for some backend code that has been provided for you.

### Task
- Your task is to build a suitable UI for a Library.
- The code for constructing a library, managing books and loans has been provided for you.
- You should not need to change any of the existing code, but you may add new functions as you see fit.
- The UI may be text based or graphical, but should allow a user to:
  - Load an existing library from a file specified, or create a new one
  - Add new books. Multiple copies of the same book (i.e. same title/author/isbn) are allowed.
  - Check if a book exists, and/or if it is available to loan to a student.
  - Remove a book from the library.
  - View a summary of all books in the library.
  - Loan a book to a student.
  - View existing loans.
  - Return a book/end a loan to a student and check if a fine is due on the loan.
  - Save a copy of the library to a file that can be read next time the program is run.
- There are no solutions provided for this project as how you approach it, and the type of UI you choose to create is 
completely up to you.

You should begin by familiarising yourself with the code for you. A summary of the code that has been written for you has been provided below:
### book.py
  - The Book class is used to store and manipulate books
  - A book has a title, author and ISBN. A book ID will be assigned automatically. 
  Books also have an `on_loan` attribute which is set to false by default and is used to determine 
  whether a book is already on loan to a student.
  - The book class is Frozen, meaning you can not append new attributes to the class.
  - You may access or update any attribute of the class via the class properties. An example of how you may use the Book class is provided below:
    - ```python 
      >>> my_book = Book('title', 'author', 123456)
      >>> my_book.title
      title
      >>> my_book.author
      author
      >>> my_book.id
      f87b616b-8ed2-47cd-89fb-c134e4c02c26
      >>> my_book.title = 'Updated Title'
      >>> my_book.title
      Updated Title
      >>> my_book.new_attr = 'Example'
      AttributeError: Cannot create new attributes on the frozen class Book
      ```
  - str, repr eq and dict methods are provided for you. ``__str__`` allows you to call `str(book)`. 
  To get the dictionary representation of a book, call `Book.__dict__()`

### loans.py
- When a book is on loan to a student, an instance of the `Loan` class is created to track that loan. 
- A global constant `FINE_PER_DAY` is used to determine how much to fine a student per day the book is overdue.
- A `Loan` must be created with a `Book`, a string indicating who the book is loaned to, and a date the book is due to 
be returned. The return date must be a valid date in the format `YYYY-MM-DD`
- The `get_fine_due` method can be used to check what fine is due if the book is returned immediately.
- An example of how you may use the `Loan` class is provided below:
  - ``` python
    >>> book_to_loan = Book('Title', 'Author', 123)
    >>> loan = Loan(book_to_loan, 'Example', '2021-12-31')
    >>> loan.book  # retuns repr(book)
    Book('Title', 'Author', 123)
    >>> loan.loaned_to
    Example
    >>> loan.due_date  # Returns a datetime object
    datetime.date(2021, 12, 31)
    >>> loan.get_fine_due()
    >>> 0
    ```

### library.py
The Library class provides an interface for managing books and loans. The functions provided as part of this class are:
- ```python
  add_book(self, title: str, author: str, isbn: int) -> None
  ```
    - Used to add a new book to the library
- ```python
  get_book(self, title: str, author: str = None, isbn: int = None, book_id: str = None) -> Iterable[Book]
   ```
  - Used to get a book from the library. Returns an iterable of potential books that match the specified criteria.
    `title` is required, all other fields are optional and will only be included as search parameters if they are provided.
- ```python
  remove_book(self, title: str, book_id: str = None) -> bool
  ```
  - Removes the specified book. `book_id` is optional, but will be used as a search parameter if provided.
    The function will return True if the book was removed successfully, and False if not.
- ```python
  book_exists(self, title: str, author: str = None, isbn: int = None) -> bool
  ```
  - Used to check if a book exists. `title` is a required search parameter, all other fields are optional, and 
    will be included as search parameters only if they are specified. Returns True if a book matching the search 
    criteria exists in the library, otherwise returns False.
- ```python
  book_is_available(self, title: str) -> bool
  ```
  - Used to check if a book with the specified title exists. Returns True if a book does exist, and False if not.
- ```python
  loan_book(self, title: str, loan_to: str, due_date: str) -> None
  ```
  - Creates a new loan for the specified book. If multiple books with the same title exist, the first available book 
    instance will be used. The function will raise an `AttributeError` if no books with the specified title 
    are available, and will raise a `ValueError` if the due_date specified is not a valid date in the format `YYYY-MM-DD`.
- ```python
  return_book(self, book_title: str, loaned_to: str, due_date: str = None) -> Optional[float]:
  ```
  - Used to return a book with the specified title that is on loan to the specified person. If the due date is 
  specified, this will be used search for the correct loan, otherwise it will be ignored. The function will return a float
  representing the fine due (if any), or raise an `AttributeError` if no loan with the specified parameters exists. 
  A `ValueError` will be raised if a `due_date` is provided that is not a valid date in the format `YYYY-MM-DD`.
- ```python
  save_library(self, file_name: str = None) -> None:
  ```
  - Used to save the library state in binary format for future use. If no file_name is provided, the library 
  will be saved to a file named `library.pkl`
  - To load a library from a file, use the `from_file` method on the Library class, for example:
    `Library.from_file('library.pkl')` will return an instance of the library class loaded from the `library.pkl` file.