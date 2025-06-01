import unittest
from flask import Flask
from controllers.book_controller import book_blueprint

class TestBookController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(book_blueprint, url_prefix='/books')
        self.client = self.app.test_client()

    def test_add_book(self):
        response = self.client.post('/books/add', json={
            "title": "Test Book",
            "author": "Test Author",
            "category": 1,
            "isbn": "1234567890",
            "publication_year": 2023,
            "publisher": "Test Publisher",
            "quantity": 10
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Book added successfully', response.get_json().get('message'))

if __name__ == '__main__':
    unittest.main()
