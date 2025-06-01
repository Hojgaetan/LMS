import unittest
from services.book_service import BookService
from models.book import Book
from models.author import Author
from models.category import Category

class TestBookService(unittest.TestCase):

    def setUp(self):
        # Mock database setup or any required initialization
        self.mock_author = Author(name="Test Author")
        self.mock_category = Category(name="Test Category")
        self.mock_book = Book(title="Test Book", author_id=2, category_id=1)

    def test_add_book(self):
        result, message = BookService.add_book(
            title="New Book",
            author_id=2,
            category_id=1,
            isbn="12345678677",
            publication_year=2023,
            publisher="Test Publisher",
            quantity=5
        )
        self.assertTrue(result)
        self.assertIsInstance(message, int)  # Expecting book ID

    def test_get_book(self):
        book = BookService.get_book(1)
        self.assertIsInstance(book, Book)

    def test_get_all_books(self):
        books = BookService.get_all_books()
        self.assertIsInstance(books, list)

    def test_search_books_by_title(self):
        books = BookService.search_books_by_title("Test")
        self.assertIsInstance(books, list)

    def test_search_books_by_author(self):
        books = BookService.search_books_by_author(1)
        self.assertIsInstance(books, list)

    def test_search_books_by_category(self):
        books = BookService.search_books_by_category(1)
        self.assertIsInstance(books, list)

    def test_update_book(self):
        result, message = BookService.update_book(18, title="Updated Title")
        self.assertTrue(result)
        self.assertIsInstance(message, int)  # Expecting book ID

    def test_delete_book(self):
        result, message = BookService.delete_book(18)
        self.assertTrue(result)
        self.assertEqual(message, "Book 'Test Book' deleted successfully")

if __name__ == "__main__":
    unittest.main()
