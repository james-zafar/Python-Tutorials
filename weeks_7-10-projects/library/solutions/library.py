from pathlib import Path

import pandas as pd

from book import Book


class Library:
    def __init__(self, name: str, books: list[Book] = None):
        self.name = name
        self.books = books or []  # type: list[Book]

    @classmethod
    def from_file(cls, name: str, file_name: str) -> 'Library':
        path = Path(file_name)
        if not path.is_file():
            raise ValueError(f'The file \'{file_name}\' does not exist, or is not a file.')
        books = pd.read_csv(file_name).tolist()

        return cls(name=name, books=books)

    def add_book(self, title: str, author: str, isbn: int) -> None:
        self.books.append(Book(title, author, isbn))

    def remove_books(self, book_id: int) -> bool:
        ...

    def book_exists(self, title: str, author: str = None, isbn: int = None):
        ...

    def book_is_available(self, title: str = None, book_id: int = None) -> bool:
        ...

    def loan_book(self, title: str) -> None:
        ...

    def library_to_df(self) -> pd.DataFrame:
        return pd.DataFrame([vars(book) for book in self.books])

    def save_library(self) -> None:
        print('Saving library state to \'library.csv\'')
        self.library_to_df().to_csv('library.csv', index=False)
