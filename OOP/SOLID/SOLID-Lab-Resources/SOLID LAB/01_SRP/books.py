from typing import Union, List


class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page: int) -> None:
        self.page = page


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str) -> Union[Book, str]:
        try:
            return [b for b in self.books if b.title == title][0]
        except IndexError:
            return "Book does not exist"


b1 = Book("Test1", "T1")
b2 = Book("Test2", "T2")
b3 = Book("Test3", "T3")
b4 = Book("Test4", "T4")

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)

print(b1.title )


