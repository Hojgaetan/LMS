import sqlite3
import os


class DatabaseConnection:
    """A utility class for managing database connections."""

    _DB_NAME = "library.db"
    #   _DB_NAME = '../library.db'

    @classmethod
    def get_db_name(cls):
        """Get the database name."""
        return cls._DB_NAME

    @classmethod
    def set_db_name(cls, db_name):
        """Set the database name."""
        cls._DB_NAME = db_name

    @classmethod
    def get_connection(cls):
        """Get a connection to the database."""
        return sqlite3.connect(cls.get_db_name())

    @classmethod
    def execute_query(cls, query, params=None):
        """Execute a query and return the result."""
        conn = cls.get_connection()
        cursor = conn.cursor()

        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = cursor.fetchall()
            conn.commit()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def execute_insert(cls, query, params=None):
        """Execute an insert or update query and return the last row id or number of rows affected."""
        conn = cls.get_connection()
        cursor = conn.cursor()

        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # For UPDATE queries, return the number of rows affected
            if query.strip().upper().startswith('UPDATE'):
                last_id = cursor.rowcount
            else:
                last_id = cursor.lastrowid
                
            conn.commit()
            return last_id
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def create_tables(cls):
        """Create the database tables if they don't exist."""
        # Check if database file exists and delete it if it does (for fresh start)
        if os.path.exists(cls.get_db_name()):
            os.remove(cls.get_db_name())

        conn = cls.get_connection()
        cursor = conn.cursor()

        # Create Authors table
        cursor.execute(
            """
        CREATE TABLE authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            biography TEXT
        )
        """
        )

        # Create Categories/Genres table
        cursor.execute(
            """
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
        """
        )

        # Create Books table
        cursor.execute(
            """
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            category_id INTEGER,
            isbn TEXT UNIQUE,
            publication_year INTEGER,
            publisher TEXT,
            quantity INTEGER DEFAULT 1,
            available_quantity INTEGER DEFAULT 1,
            FOREIGN KEY (author_id) REFERENCES authors (author_id),
            FOREIGN KEY (category_id) REFERENCES categories (category_id)
        )
        """
        )

        # Create Members/Users table
        cursor.execute(
            """
        CREATE TABLE members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT,
            registration_date TEXT DEFAULT CURRENT_TIMESTAMP,
        )
        """
        )

        # Create Borrowing records table
        cursor.execute(
            """
        CREATE TABLE borrowings (
            borrowing_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            borrow_date TEXT DEFAULT CURRENT_TIMESTAMP,
            due_date TEXT NOT NULL,
            return_date TEXT,
            status TEXT DEFAULT 'borrowed',
            FOREIGN KEY (book_id) REFERENCES books (book_id),
            FOREIGN KEY (member_id) REFERENCES members (member_id)
        )
        """
        )

        conn.commit()
        conn.close()

    @classmethod
    def insert_sample_data(cls):
        """Insert sample data into the database."""
        conn = cls.get_connection()
        cursor = conn.cursor()

        # Sample authors
        cursor.execute(
            "INSERT INTO authors (name, biography) VALUES (?, ?)",
            ("Victor Hugo", "French poet, novelist, and dramatist of the Romantic movement"),
        )
        cursor.execute(
            "INSERT INTO authors (name, biography) VALUES (?, ?)",
            ("J.K. Rowling", "British author, philanthropist, film producer, and screenwriter"),
        )

        # Sample categories
        cursor.execute(
            "INSERT INTO categories (name, description) VALUES (?, ?)", ("Fiction", "Literary works created from the imagination")
        )
        cursor.execute(
            "INSERT INTO categories (name, description) VALUES (?, ?)",
            ("Science Fiction", "Fiction based on scientific discoveries or advanced technology"),
        )
        cursor.execute("INSERT INTO categories (name, description) VALUES (?, ?)", ("History", "Books about past events"))

        # Sample books
        cursor.execute(
            "INSERT INTO books (title, author_id, category_id, isbn, publication_year, publisher, quantity, available_quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ("Les Misérables", 1, 1, "9780451419439", 1862, "A. Lacroix", 3, 3),
        )
        cursor.execute(
            "INSERT INTO books (title, author_id, category_id, isbn, publication_year, publisher, quantity, available_quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ("Harry Potter and the Philosopher's Stone", 2, 1, "9780747532699", 1997, "Bloomsbury", 5, 5),
        )

        # Sample members
        cursor.execute(
            "INSERT INTO members (name, email, phone, address) VALUES (?, ?, ?, ?)",
            ("Jean Dupont", "jean.dupont@email.com", "0123456789", "123 Rue de Paris"),
        )
        cursor.execute(
            "INSERT INTO members (name, email, phone, address) VALUES (?, ?, ?, ?)",
            ("Marie Martin", "marie.martin@email.com", "9876543210", "456 Avenue des Champs"),
        )

        conn.commit()
        conn.close()

        print("Sample data inserted successfully!")
