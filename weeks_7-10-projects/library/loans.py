from datetime import datetime
from typing import Final

from .book import Book


class Loan:
    FINE_PER_DAY: Final[float] = 0.99

    def __init__(self, book: Book, loaned_to: str, due_date: str) -> None:
        self.book = book
        self.loaned_to = loaned_to
        try:
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('The \'due_date\' must be a valid date in the format YYYY-MM-DD')

        self.fine_due = 0.

    def get_fine_due(self) -> float:
        current_date = datetime.now().date()
        days_overdue = current_date - self.due_date
        if overdue := days_overdue.days > 0:
            return overdue * self.FINE_PER_DAY
        return 0

    def return_book(self) -> None:
        self.book.on_loan = False

    def __dict__(self) -> dict[str, str]:
        return {
            'book': self.book.__dict__,
            'loaned_to': self.loaned_to,
            'due_date': self.due_date.strftime('%Y-%m-%d')

        }

    def __str__(self) -> str:
        return f'{str(self.book)}, loaned to: {self.loaned_to}, and is due to be returned on {self.due_date}.'

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}({self.book!r}, {self.loaned_to!r}, {self.due_date!r})'
