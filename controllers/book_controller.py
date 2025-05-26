from models.book import Book
from models.author import Author
from models.category import Category


class BookController:
    """Controller class for book-related operations."""

    @staticmethod
    def add_book(title, author_id, category_id, isbn=None, publication_year=None, publisher=None, quantity=1):
        """
        Add a new book to the library.

        Args:
            title (str): The title of the book
            author_id (int): The ID of the author
            category_id (int): The ID of the category
            isbn (str, optional): The ISBN of the book
            publication_year (int, optional): The year the book was published
            publisher (str, optional): The publisher of the book
            quantity (int, optional): The number of copies available, defaults to 1

        Returns:
            tuple: (success, result) where success is a boolean indicating if the operation was successful
                  and result is either the book ID or an error message
        """
        # Create a new book instance
        book = Book(
            title=title,
            author_id=author_id,
            category_id=category_id,
            isbn=isbn,
            publication_year=publication_year,
            publisher=publisher,
            quantity=quantity,
            available_quantity=quantity,
        )

        # Validate the book data
        is_valid, message = book.validate()
        if not is_valid:
            return False, message

        # Save the book to the database
        book_id = book.save()
        if book_id:
            return True, book_id
        else:
            return False, "Failed to save book to database"

    @staticmethod
    def get_book(book_id):
        """
        Get a book by its ID.

        Args:
            book_id (int): The ID of the book to retrieve

        Returns:
            Book: The book with the given ID, or None if not found
        """
        return Book.find_by_id(book_id)

    @staticmethod
    def get_all_books():
        """
        Get all books in the library.

        Returns:
            list: A list of all books
        """
        return Book.find_all()

    @staticmethod
    def search_books_by_title(title):
        """
        Search for books by title.

        Args:
            title (str): The title to search for

        Returns:
            list: A list of books matching the search criteria
        """
        return Book.find_by_title(title)

    @staticmethod
    def search_books_by_author(author_id):
        """
        Search for books by author.

        Args:
            author_id (int): The ID of the author

        Returns:
            list: A list of books by the specified author
        """
        return Book.find_by_author(author_id)

    @staticmethod
    def search_books_by_category(category_id):
        """
        Search for books by category.

        Args:
            category_id (int): The ID of the category

        Returns:
            list: A list of books in the specified category
        """
        return Book.find_by_category(category_id)

    @staticmethod
    def update_book(book_id, **kwargs):
        """
        Update a book's information.

        Args:
            book_id (int): The ID of the book to update
            **kwargs: The fields to update and their new values

        Returns:
            tuple: (success, result) where success is a boolean indicating if the operation was successful
                  and result is either the book ID or an error message
        """
        book = Book.find_by_id(book_id)
        if not book:
            return False, f"Book with ID {book_id} not found"

        # Update the book's attributes
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)

        # Validate the updated book data
        is_valid, message = book.validate()
        if not is_valid:
            return False, message

        # Save the updated book to the database
        book_id = book.save()
        if book_id:
            return True, book_id
        else:
            return False, "Failed to update book in database"

    @staticmethod
    def delete_book(book_id):
        """
        Delete a book from the library.

        Args:
            book_id (int): The ID of the book to delete

        Returns:
            tuple: (success, message) where success is a boolean indicating if the operation was successful
                  and message is a string describing the result
        """
        book = Book.find_by_id(book_id)
        if not book:
            return False, f"Book with ID {book_id} not found"

        try:
            book.delete()
            return True, f"Book '{book.title}' deleted successfully"
        except Exception as e:
            return False, f"Failed to delete book: {str(e)}"

    @staticmethod
    def remove_book(book_id):
        """
        Remove a book from the library by its ID.
        Args:
            book_id (int): The ID of the book to remove
        Returns:
            tuple: (success, message) where success is a boolean and message is a string
        """
        from models.book import Book

        # Check if the book exists
        book = Book.find_by_id(book_id)
        if not book:
            return False, f"Book with ID {book_id} does not exist."
        # Delete the book
        success = Book.delete(book_id)
        if success:
            return True, f"Book with ID {book_id} has been removed."
        else:
            return False, "Failed to remove the book."

    @staticmethod
    def get_all_authors():
        """
        Get all authors in the library.

        Returns:
            list: A list of all authors
        """
        return Author.find_all()

    @staticmethod
    def get_all_categories():
        """
        Get all categories in the library.

        Returns:
            list: A list of all categories
        """
        return Category.find_all()
