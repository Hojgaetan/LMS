from models.base_model import BaseModel
from utils.db_utils import DatabaseConnection

class Author(BaseModel):
    """Model class for authors."""

    TABLE_NAME = 'authors'
    PRIMARY_KEY = 'author_id'

    def __init__(self, author_id=None, name=None, biography=None, **kwargs):
        """Initialize an Author instance."""
        super().__init__(**kwargs)
        self.author_id = author_id
        self.name = name
        self.biography = biography

    @property
    def author_id(self):
        """Get the author ID."""
        return self._get_attribute('author_id')

    @author_id.setter
    def author_id(self, value):
        """Set the author ID."""
        self._set_attribute('author_id', value)

    @property
    def name(self):
        """Get the author name."""
        return self._get_attribute('name')

    @name.setter
    def name(self, value):
        """Set the author name."""
        self._set_attribute('name', value)

    @property
    def biography(self):
        """Get the author biography."""
        return self._get_attribute('biography')

    @biography.setter
    def biography(self, value):
        """Set the author biography."""
        self._set_attribute('biography', value)

    @classmethod
    def find_by_name(cls, name):
        """Find authors by name (partial match)."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE name LIKE ?"
        results = DatabaseConnection.execute_query(query, (f"%{name}%",))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    def get_books(self):
        """Get all books by this author."""
        from models.book import Book
        return Book.find_by_author(self.author_id)

    def validate(self):
        """Validate the author data."""
        if not self.name:
            return False, "Author name is required"

        return True, "Author is valid"
