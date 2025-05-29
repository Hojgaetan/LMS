from models.base_model import BaseModel
from utils.db_utils import DatabaseConnection


class Category(BaseModel):
    """Model class for categories."""

    TABLE_NAME = "categories"
    PRIMARY_KEY = "category_id"

    def __init__(self, category_id=None, name=None, description=None, **kwargs):
        """Initialize a Category instance."""
        super().__init__(**kwargs)
        self.category_id = category_id
        self.name = name
        self.description = description

    @property
    def category_id(self):
        """Get the category ID."""
        return self._get_attribute("category_id")

    @category_id.setter
    def category_id(self, value):
        """Set the category ID."""
        self._set_attribute("category_id", value)

    @property
    def name(self):
        """Get the category name."""
        return self._get_attribute("name")

    @name.setter
    def name(self, value):
        """Set the category name."""
        self._set_attribute("name", value)

    @property
    def description(self):
        """Get the category description."""
        return self._get_attribute("description")

    @description.setter
    def description(self, value):
        """Set the category description."""
        self._set_attribute("description", value)

    @classmethod
    def find_by_name(cls, name):
        """Find categories by name (partial match)."""
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

    @classmethod
    def all(cls):
        """Return all categories from the database as a list of Category objects."""
        query = f"SELECT * FROM {cls.TABLE_NAME}"
        results = DatabaseConnection.execute_query(query)
        if results:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()
            return [cls(**dict(zip(columns, result))) for result in results]
        return []

    def get_books(self):
        """Get all books in this category."""
        from models.book import Book

        return Book.find_by_category(self.category_id)

    def validate(self):
        """Validate the category data."""
        if not self.name:
            return False, "Category name is required"

        return True, "Category is valid"
    
    @classmethod
    def count(cls):
        """Count the total number of categories."""
        query = f"SELECT COUNT(*) FROM {cls.TABLE_NAME}"
        result = DatabaseConnection.execute_query(query)
        return result[0][0] if result else 0
