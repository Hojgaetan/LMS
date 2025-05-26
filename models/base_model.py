from utils.db_utils import DatabaseConnection


class BaseModel:
    """Base class for all models."""

    TABLE_NAME = None
    PRIMARY_KEY = None

    def __init__(self, **kwargs):
        """Initialize a model instance with the given attributes."""
        self._attributes = {}
        for key, value in kwargs.items():
            self._set_attribute(key, value)

    def _get_attribute(self, name):
        """Get an attribute value."""
        return self._attributes.get(name)

    def _set_attribute(self, name, value):
        """Set an attribute value."""
        self._attributes[name] = value

    def __getattr__(self, name):
        """Handle attribute access for non-existent attributes."""
        if name in self._attributes:
            return self._get_attribute(name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Handle attribute assignment."""
        if name == "_attributes":
            # Allow direct assignment for the _attributes dictionary
            super().__setattr__(name, value)
        else:
            # Store all other attributes in the _attributes dictionary
            self._set_attribute(name, value)

    @property
    def __dict__(self):
        """Return a dictionary of attributes for compatibility with existing code."""
        return self._attributes.copy()

    @classmethod
    def find_by_id(cls, id: int):
        """Find a record by its primary key."""
        if not cls.TABLE_NAME or not cls.PRIMARY_KEY:
            raise NotImplementedError("TABLE_NAME and PRIMARY_KEY must be defined in subclass")

        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE {cls.PRIMARY_KEY} = ?"
        result = DatabaseConnection.execute_query(query, (id,))

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
    def find_all(cls):
        """Find all records in the table."""
        if not cls.TABLE_NAME:
            raise NotImplementedError("TABLE_NAME must be defined in subclass")

        query = f"SELECT * FROM {cls.TABLE_NAME}"
        results = DatabaseConnection.execute_query(query)

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    def save(self):
        """Save the model to the database (insert or update)."""
        if not self.__class__.TABLE_NAME or not self.__class__.PRIMARY_KEY:
            raise NotImplementedError("TABLE_NAME and PRIMARY_KEY must be defined in subclass")

        # Get all attributes of the instance
        attributes = self._attributes

        # Check if the record already exists
        primary_key_value = attributes.get(self.__class__.PRIMARY_KEY)
        if primary_key_value:
            # Update existing record
            set_clause = ", ".join([f"{key} = ?" for key in attributes.keys() if key != self.__class__.PRIMARY_KEY])
            values = [value for key, value in attributes.items() if key != self.__class__.PRIMARY_KEY]
            values.append(primary_key_value)  # Add the primary key value for the WHERE clause

            query = f"UPDATE {self.__class__.TABLE_NAME} SET {set_clause} WHERE {self.__class__.PRIMARY_KEY} = ?"
            DatabaseConnection.execute_query(query, values)
            return primary_key_value
        else:
            # Insert new record
            columns = ", ".join(attributes.keys())
            placeholders = ", ".join(["?"] * len(attributes))
            values = list(attributes.values())

            query = f"INSERT INTO {self.__class__.TABLE_NAME} ({columns}) VALUES ({placeholders})"
            new_id = DatabaseConnection.execute_insert(query, values)

            # Update the instance with the new ID
            self._set_attribute(self.__class__.PRIMARY_KEY, new_id)
            return new_id

    def delete(self):
        """Delete the model from the database."""
        if not self.__class__.TABLE_NAME or not self.__class__.PRIMARY_KEY:
            raise NotImplementedError("TABLE_NAME and PRIMARY_KEY must be defined in subclass")

        primary_key_value = self._get_attribute(self.__class__.PRIMARY_KEY)
        if not primary_key_value:
            raise ValueError(f"{self.__class__.PRIMARY_KEY} is not set")

        query = f"DELETE FROM {self.__class__.TABLE_NAME} WHERE {self.__class__.PRIMARY_KEY} = ?"
        DatabaseConnection.execute_query(query, (primary_key_value,))
