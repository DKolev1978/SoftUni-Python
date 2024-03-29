from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def test_correct_initialization(self):
        bookstore = Bookstore(10)
        self.assertEqual(10, bookstore.books_limit)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore.total_sold_books)

    def test_books_limit_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            bookstore = Bookstore(-1)

        self.assertEqual(str(ve.exception), f"Books limit of -1 is not valid")

    def test_books_limit_setter_works_correctly(self):
        bookstore = Bookstore(11)
        self.assertEqual(bookstore.books_limit, 11)

    def test_len_works_correctly(self):
        bookstore = Bookstore(11)
        bookstore.availability_in_store_by_book_titles["Test1"] = 1
        bookstore.availability_in_store_by_book_titles["Test2"] = 3
        result = bookstore.__len__()
        self.assertEqual(result, 4)


if __name__ == "__main__":
    main()
