import sqlite3


def get_all_authors():
    """Retrieve all authors from the database."""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT author_id, name FROM authors")
    authors = cursor.fetchall()
    conn.close()
    return authors


def get_all_categories():
    """Retrieve all categories from the database."""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category_id, name FROM categories")
    categories = cursor.fetchall()
    conn.close()
    return categories


def add_book(title, author_id, category_id, isbn=None, publication_year=None, publisher=None, quantity=1):
    """
    Add a new book to the library database.

    Args:
        title (str): The title of the book (required)
        author_id (int): The ID of the author (required)
        category_id (int): The ID of the category (required)
        isbn (str, optional): The ISBN of the book
        publication_year (int, optional): The year the book was published
        publisher (str, optional): The publisher of the book
        quantity (int, optional): The number of copies available, defaults to 1

    Returns:
        int: The ID of the newly added book, or None if the operation failed
    """
    # Validate required fields
    if not title:
        print("Error: Book title is required")
        return None

    if not author_id:
        print("Error: Author ID is required")
        return None

    if not category_id:
        print("Error: Category ID is required")
        return None

    try:
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Check if author exists
        cursor.execute("SELECT author_id FROM authors WHERE author_id = ?", (author_id,))
        if not cursor.fetchone():
            print(f"Error: Author with ID {author_id} does not exist")
            conn.close()
            return None

        # Check if category exists
        cursor.execute("SELECT category_id FROM categories WHERE category_id = ?", (category_id,))
        if not cursor.fetchone():
            print(f"Error: Category with ID {category_id} does not exist")
            conn.close()
            return None

        # Check if ISBN already exists (if provided)
        if isbn:
            cursor.execute("SELECT book_id FROM books WHERE isbn = ?", (isbn,))
            if cursor.fetchone():
                print(f"Error: A book with ISBN {isbn} already exists")
                conn.close()
                return None

        # Insert the new book
        cursor.execute(
            """
        INSERT INTO books (title, author_id, category_id, isbn, publication_year, 
                          publisher, quantity, available_quantity) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (title, author_id, category_id, isbn, publication_year, publisher, quantity, quantity),
        )

        book_id = cursor.lastrowid
        conn.commit()
        conn.close()

        print(f"Book '{title}' added successfully with ID: {book_id}")
        return book_id

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
