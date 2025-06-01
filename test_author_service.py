import unittest
from services.author_service import AuthorService
from models.author import Author

class TestAuthorService(unittest.TestCase):

    def setUp(self):
        # Mock database setup or any required initialization
        self.mock_author = Author(name="Test Author", biography="Test Biography")

    def test_add_author(self):
        result, message = AuthorService.add_author("New Author", "Biography")
        self.assertTrue(result)
        self.assertEqual(message, "Author 'New Author' added successfully.")

    def test_update_author(self):
        # Assuming author with ID 1 exists
        result, message = AuthorService.update_author(15, name="Updated Name", biography="Updated Biography")
        self.assertTrue(result)
        self.assertEqual(message, "Author '15' updated successfully.")

    def test_delete_author(self):
        # Assuming author with ID 1 exists
        result, message = AuthorService.delete_author(13)
        self.assertTrue(result)
        self.assertEqual(message, "Author '13' deleted successfully.")

    def test_list_authors(self):
        authors = AuthorService.list_authors()
        self.assertIsInstance(authors, list)

    def test_search_authors_by_name(self):
        authors = AuthorService.search_authors_by_name("Test")
        self.assertIsInstance(authors, list)

    def test_count_authors(self):
        count = AuthorService.count_authors()
        self.assertIsInstance(count, int)

    def test_get_author_name(self):
        # Assuming author with ID 1 exists
        name = AuthorService.get_author_name(3)
        self.assertIsInstance(name, str)

if __name__ == "__main__":
    unittest.main()
