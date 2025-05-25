import os
from controllers.database_controller import DatabaseController
from controllers.book_controller import BookController
from models.book import Book

def test_add_book():
    """Test the add_book functionality."""
    print("Testing add_book functionality...")

    # Initialize the database for testing
    DatabaseController.initialize_database(force_reset=True)
    print("Database created for testing.")

    # Create a book controller
    book_controller = BookController()

    # Get all authors and categories
    authors = book_controller.get_all_authors()
    categories = book_controller.get_all_categories()

    print("\nAvailable Authors:")
    for author in authors:
        print(f"{author.author_id}. {author.name}")

    print("\nAvailable Categories:")
    for category in categories:
        print(f"{category.category_id}. {category.name}")

    # Test adding a new book
    print("\nAdding a new test book...")
    book_title = "Test Book Title"
    author_id = 1  # Using the first author from the database
    category_id = 1  # Using the first category from the database
    isbn = "9781234567890"
    publication_year = 2023
    publisher = "Test Publisher"
    quantity = 3

    # Check if a book with this ISBN already exists and remove it
    existing_book = Book.find_by_isbn(isbn)
    if existing_book:
        print(f"A book with ISBN {isbn} already exists. Removing it for the test...")
        existing_book.delete()

    # Add the book using the controller
    success, result = book_controller.add_book(
        title=book_title, 
        author_id=author_id, 
        category_id=category_id, 
        isbn=isbn, 
        publication_year=publication_year, 
        publisher=publisher, 
        quantity=quantity
    )

    # Verify the book was added
    if success:
        book_id = result
        print(f"\nBook added successfully with ID: {book_id}")

        # Verify the book exists in the database
        book = Book.find_by_id(book_id)

        if book:
            print("\nVerification successful: Book found in database")
            print(f"Book details: {book.__dict__}")
            return True
        else:
            print("\nVerification failed: Book not found in database")
            return False
    else:
        print(f"\nFailed to add book: {result}")
        return False

if __name__ == "__main__":
    test_result = test_add_book()
    if test_result:
        print("\nTest passed: Book management functionality is working correctly.")
    else:
        print("\nTest failed: Book management functionality is not working correctly.")
