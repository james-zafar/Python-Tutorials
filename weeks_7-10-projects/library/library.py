import pickle
from collections.abc import Iterable
from datetime import datetime
from pathlib import Path
from typing import Optional

from .book import Book
from .loans import Loan


class Library:
    def __init__(self, name: str, books: list[Book] = None, loans: list[str] = None) -> None:
        self.name = name
        self._books = books or []  # type: list[Book]
        self._loans = loans or []  # type: list[Loan]

    @property
    def books(self) -> list[Book]:
        return self._books

    @property
    def active_loans(self) -> list[Loan]:
        return self._loans

    @classmethod
    def from_file(cls, file_name: str, ) -> 'Library':
        library_path = Path(file_name)
        if not library_path.is_file():
            raise ValueError(f'\'{file_name}\' is not a valid file, or does not exist.')
        with open(file_name, 'rb') as f:
            library = pickle.load(f)

        return library

    def add_book(self, title: str, author: str, isbn: int) -> None:
        self.books.append(Book(title, author, isbn))

    def get_book(self, title: str, author: str = None, isbn: int = None, book_id: str = None) -> Iterable[Book]:
        if book_id:
            return filter(lambda book_: book_.id == book_id, self.books)
        return filter(lambda ele: ele.title == title and (ele.author == author if author else ...) and
                                  (ele.isbn == isbn if isbn else ...) and (ele.id == book_id if book_id else ...), self.books)

    def remove_book(self, title: str, book_id: str = None) -> bool:
        possible_books = filter(lambda book_: book_.title == title and (book_.id == book_id if book_id else ...),
                                self.books)
        if book := next(possible_books, None):
            self.books.remove(book)
            return True
        return False

    def book_exists(self, title: str, author: str = None, isbn: int = None) -> bool:
        books = filter(lambda book_: book_.title == title and (book_.author == author if author else ...)
                                     and (book_.isbn == isbn if isbn else ...), self.books)

        return next(books, None) is not None

    def book_is_available(self, title: str) -> bool:
        for book in self.books:
            if book.title == title and not book.on_loan:
                return True
        return False

    def loan_book(self, title: str, loan_to: str, due_date: str) -> None:
        for book in self.books:
            if book.title == title and not book.on_loan:
                book.on_loan = True
                self._loans.append(Loan(book, loan_to, due_date))
                return
        raise AttributeError(f'No books with the title \'{title}\' are available to loan at this time.')

    def return_book(self, book_title: str, loaned_to: str, due_date: str = None) -> Optional[float]:
        if due_date:
            try:
                due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError('The \'due_date\' must be a valid date in the format YYYY-MM-DD')
        loans = list(filter(lambda loan_: loan_.book.title == book_title
                                          and (loan_.loaned_to == loaned_to if loaned_to else ...)
                                          and (loan_.due_date == due_date if due_date else ...), self._loans))
        if len(loans) == 0:
            raise AttributeError(f'No loan exists for a book with title \'{book_title}\', that is currently on loan to {loaned_to}')
        fine_due = loans[0].get_fine_due()
        loans[0].return_book()

        return fine_due or None

    def save_library(self, file_name: str = None) -> None:
        if file_name and not file_name.endswith('.pkl'):
            file_name = f'{file_name}.pkl'
        else:
            file_name = 'library.pkl'

        print(f'Saving library state to \'{file_name}\'')
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
