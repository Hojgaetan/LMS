import unittest
from models.book import Book
from utils.db_utils import DatabaseConnection

class TestBookModel(unittest.TestCase):

    def setUp(self):
        # Set up a mock database connection or test data
        self.mock_data = {
            "book_id": 1,
            "title": "Test Book",
            "author_id": 1,
            "category_id": 1,
            "isbn": "1234567890",
            "publication_year": 2023,
            "publisher": "Test Publisher",
            "quantity": 10,
            "available_quantity": 10
        }
        self.book = Book(**self.mock_data)

    def test_validate(self):
        # Test validation logic
        is_valid, message = self.book.validate()
        self.assertTrue(is_valid)
        self.assertEqual(message, "Book is valid")

    def test_find_by_isbn(self):
        # Mock the database query
        DatabaseConnection.execute_query = lambda query, params: [tuple(self.mock_data.values())]
        book = Book.find_by_isbn("1234567890")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Test Book")

    def test_find_by_title(self):
        # Mock the database query
        DatabaseConnection.execute_query = lambda query, params: [tuple(self.mock_data.values())]
        books = Book.find_by_title("Test Book")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

if __name__ == "__main__":
    unittest.main()
