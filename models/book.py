from models.base_model import BaseModel
from utils.db_utils import DatabaseConnection

class Book(BaseModel):
    """Model class for books."""

    TABLE_NAME = 'books'
    PRIMARY_KEY = 'book_id'

    def __init__(self, book_id=None, title=None, author_id=None, category_id=None, 
                 isbn=None, publication_year=None, publisher=None, quantity=1, 
                 available_quantity=None, **kwargs):
        """Initialize a Book instance."""
        super().__init__(**kwargs)
        self.book_id = book_id
        self.title = title
        self.author_id = author_id
        self.category_id = category_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.publisher = publisher
        self.quantity = quantity
        self.available_quantity = available_quantity if available_quantity is not None else quantity

    @property
    def book_id(self):
        """Get the book ID."""
        return self._get_attribute('book_id')

    @book_id.setter
    def book_id(self, value):
        """Set the book ID."""
        self._set_attribute('book_id', value)

    @property
    def title(self):
        """Get the book title."""
        return self._get_attribute('title')

    @title.setter
    def title(self, value):
        """Set the book title."""
        self._set_attribute('title', value)

    @property
    def author_id(self):
        """Get the author ID."""
        return self._get_attribute('author_id')

    @author_id.setter
    def author_id(self, value):
        """Set the author ID."""
        self._set_attribute('author_id', value)

    @property
    def category_id(self):
        """Get the category ID."""
        return self._get_attribute('category_id')

    @category_id.setter
    def category_id(self, value):
        """Set the category ID."""
        self._set_attribute('category_id', value)

    @property
    def isbn(self):
        """Get the ISBN."""
        return self._get_attribute('isbn')

    @isbn.setter
    def isbn(self, value):
        """Set the ISBN."""
        self._set_attribute('isbn', value)

    @property
    def publication_year(self):
        """Get the publication year."""
        return self._get_attribute('publication_year')

    @publication_year.setter
    def publication_year(self, value):
        """Set the publication year."""
        self._set_attribute('publication_year', value)

    @property
    def publisher(self):
        """Get the publisher."""
        return self._get_attribute('publisher')

    @publisher.setter
    def publisher(self, value):
        """Set the publisher."""
        self._set_attribute('publisher', value)

    @property
    def quantity(self):
        """Get the quantity."""
        return self._get_attribute('quantity')

    @quantity.setter
    def quantity(self, value):
        """Set the quantity."""
        self._set_attribute('quantity', value)

    @property
    def available_quantity(self):
        """Get the available quantity."""
        return self._get_attribute('available_quantity')

    @available_quantity.setter
    def available_quantity(self, value):
        """Set the available quantity."""
        self._set_attribute('available_quantity', value)

    @classmethod
    def find_by_isbn(cls, isbn):
        """Find a book by its ISBN."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE isbn = ?"
        result = DatabaseConnection.execute_query(query, (isbn,))

        if result and len(result) > 0:
            # Convert the result tuple to a dictionary using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            record_dict = dict(zip(columns, result[0]))
            return cls(**record_dict)

        return None

    @classmethod
    def find_by_title(cls, title):
        """Find books by title (partial match)."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE title LIKE ?"
        results = DatabaseConnection.execute_query(query, (f"%{title}%",))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    @classmethod
    def find_by_author(cls, author_id):
        """Find books by author ID."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE author_id = ?"
        results = DatabaseConnection.execute_query(query, (author_id,))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    @classmethod
    def find_by_category(cls, category_id):
        """Find books by category ID."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE category_id = ?"
        results = DatabaseConnection.execute_query(query, (category_id,))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    @classmethod
    def delete(cls, book_id):
        """Delete a book by its ID."""
        if not cls.TABLE_NAME or not cls.PRIMARY_KEY:
            raise NotImplementedError("TABLE_NAME and PRIMARY_KEY must be defined in subclass")
        query = f"DELETE FROM {cls.TABLE_NAME} WHERE {cls.PRIMARY_KEY} = ?"
        result = DatabaseConnection.execute_query(query, (book_id,))
        return result is not None

    def get_author(self):
        """Get the author of this book."""
        from models.author import Author
        return Author.find_by_id(self.author_id)

    def get_category(self):
        """Get the category of this book."""
        from models.category import Category
        return Category.find_by_id(self.category_id)

    def validate(self):
        """Validate the book data."""
        if not self.title:
            return False, "Book title is required"

        if not self.author_id:
            return False, "Author ID is required"

        if not self.category_id:
            return False, "Category ID is required"

        # Check if author exists
        from models.author import Author
        author = Author.find_by_id(self.author_id)
        if not author:
            return False, f"Author with ID {self.author_id} does not exist"

        # Check if category exists
        from models.category import Category
        category = Category.find_by_id(self.category_id)
        if not category:
            return False, f"Category with ID {self.category_id} does not exist"

        # Check if ISBN already exists (if provided)
        if self.isbn and not self.book_id:
            existing_book = Book.find_by_isbn(self.isbn)
            if existing_book:
                return False, f"A book with ISBN {self.isbn} already exists"

        return True, "Book is valid"

