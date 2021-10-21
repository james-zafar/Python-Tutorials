import uuid
from typing import TypeVar, Union

T = TypeVar('T')


class FrozenInstance:
    _frozen = False

    def __setattr__(self, key: str, value: T) -> None:
        if self._frozen and not hasattr(self, key):
            raise AttributeError(f"Cannot create new attributes on the frozen class {self.__class__.__qualname__}")

        object.__setattr__(self, key, value)

    def _freeze(self):
        self._frozen = True


class Book(FrozenInstance):
    def __init__(self, title: str, author: str, isbn: int):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._id = uuid.uuid4()
        self._on_loan = False

        self._freeze()

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> int:
        return self._isbn

    @property
    def on_loan(self) -> bool:
        return self._on_loan

    @on_loan.setter
    def on_loan(self, value: bool) -> None:
        self._on_loan = value

    @property
    def id(self) -> str:
        return str(self._id)

    def __dict__(self) -> dict[str, Union[str, int, bool]]:
        return {
            'title': self._title,
            'author': self._author,
            'isbn': self._isbn,
            'id': self._id,
            'on_loan': self._on_loan
        }

    def __str__(self) -> str:
        return f'{self.id = }, {self.title = }, {self.author = }, {self.isbn = }, Available? {self._on_loan}'

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}({self._title!r}, {self._author!r}, {self._isbn!r})'

    def __eq__(self, other: 'Book') -> bool:
        return self._title == other._title and self._author == other._author and self._isbn == other._isbn
