import os
from utils.db_utils import DatabaseConnection

class DatabaseController:
    """Controller class for database operations."""

    @staticmethod
    def initialize_database(force_reset=False):
        """
        Initialize the database by creating tables and inserting sample data.

        Args:
            force_reset (bool): If True, the database will be reset even if it already exists

        Returns:
            bool: True if the database was initialized successfully, False otherwise
        """
        try:
            # Check if database exists
            if os.path.exists(DatabaseConnection.get_db_name()) and not force_reset:
                print(f"Database '{DatabaseConnection.get_db_name()}' already exists.")
                return True

            # Create tables
            DatabaseConnection.create_tables()
            print("Database tables created successfully.")

            # Insert sample data
            DatabaseConnection.insert_sample_data()

            return True
        except Exception as e:
            print(f"Error initializing database: {str(e)}")
            return False

    @staticmethod
    def reset_database():
        """
        Reset the database by deleting it and recreating it with sample data.

        Returns:
            bool: True if the database was reset successfully, False otherwise
        """
        return DatabaseController.initialize_database(force_reset=True)
