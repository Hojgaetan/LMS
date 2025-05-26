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

def test_update_book():
    """Test the update_book functionality."""
    print("Testing update_book functionality...")

    # Initialize the database for testing
    DatabaseController.initialize_database(force_reset=True)
    print("Database created for testing.")

    # Create a book controller
    book_controller = BookController()

    # Get all authors and categories
    authors = book_controller.get_all_authors()
    categories = book_controller.get_all_categories()

    # First, add a book to update
    print("\nAdding a test book to update...")
    book_title = "Original Book Title"
    author_id = 1  # Using the first author from the database
    category_id = 1  # Using the first category from the database
    isbn = "9781234567890"
    publication_year = 2023
    publisher = "Original Publisher"
    quantity = 3

    # Check if a book with this ISBN already exists and remove it
    existing_book = Book.find_by_isbn(isbn)
    if existing_book:
        print(f"A book with ISBN {isbn} already exists. Removing it for the test...")
        existing_book.delete()

    # Add the book using the controller
    success, book_id = book_controller.add_book(
        title=book_title, 
        author_id=author_id, 
        category_id=category_id, 
        isbn=isbn, 
        publication_year=publication_year, 
        publisher=publisher, 
        quantity=quantity
    )

    if not success:
        print(f"\nFailed to add book for update test: {book_id}")
        return False

    print(f"\nBook added successfully with ID: {book_id}")

    # Display the original book details
    original_book = Book.find_by_id(book_id)
    print("\nOriginal book details:")
    print(f"Title: {original_book.title}")
    print(f"Author ID: {original_book.author_id}")
    print(f"Category ID: {original_book.category_id}")
    print(f"ISBN: {original_book.isbn}")
    print(f"Publication Year: {original_book.publication_year}")
    print(f"Publisher: {original_book.publisher}")
    print(f"Quantity: {original_book.quantity}")

    # Test 1: Update the book with new information
    print("\nTest 1: Updating book with new information...")
    updated_title = "Updated Book Title"
    updated_publisher = "Updated Publisher"
    updated_quantity = 5

    success, result = book_controller.update_book(
        book_id,
        title=updated_title,
        publisher=updated_publisher,
        quantity=updated_quantity
    )

    if success:
        print(f"\nBook updated successfully with ID: {result}")

        # Verify the book was updated correctly
        updated_book = Book.find_by_id(book_id)

        if (updated_book.title == updated_title and 
            updated_book.publisher == updated_publisher and 
            updated_book.quantity == updated_quantity):
            print("\nVerification successful: Book updated correctly")
            print(f"Updated book details: {updated_book.__dict__}")
        else:
            print("\nVerification failed: Book not updated correctly")
            print(f"Expected title: {updated_title}, got: {updated_book.title}")
            print(f"Expected publisher: {updated_publisher}, got: {updated_book.publisher}")
            print(f"Expected quantity: {updated_quantity}, got: {updated_book.quantity}")
            return False
    else:
        print(f"\nFailed to update book: {result}")
        return False

    # Test 2: Try to update a non-existent book
    print("\nTest 2: Trying to update a non-existent book...")
    non_existent_id = 9999  # Assuming this ID doesn't exist
    success, result = book_controller.update_book(
        non_existent_id,
        title="This Should Fail"
    )

    if not success:
        print(f"\nExpected failure occurred: {result}")
    else:
        print("\nTest failed: Was able to update a non-existent book")
        return False

    # Test 3: Try to update with invalid data
    print("\nTest 3: Trying to update with invalid data (non-existent author)...")
    invalid_author_id = 9999  # Assuming this author ID doesn't exist
    success, result = book_controller.update_book(
        book_id,
        author_id=invalid_author_id
    )

    if not success:
        print(f"\nExpected failure occurred: {result}")
    else:
        print("\nTest failed: Was able to update with invalid author ID")
        return False

    # Test 4: Update with empty updates (should not change anything)
    print("\nTest 4: Updating with empty updates...")
    success, result = book_controller.update_book(
        book_id
    )

    if success:
        print(f"\nBook updated successfully with ID: {result}")
        # The book should remain unchanged
        unchanged_book = Book.find_by_id(book_id)
        if (unchanged_book.title == updated_title and 
            unchanged_book.publisher == updated_publisher and 
            unchanged_book.quantity == updated_quantity):
            print("\nVerification successful: Book remained unchanged")
        else:
            print("\nVerification failed: Book changed unexpectedly")
            return False
    else:
        print(f"\nFailed to update book: {result}")
        return False

    print("\nAll update book tests passed!")
    return True

def run_all_tests():
    """Run all book management tests."""
    print("\n===== Running All Book Management Tests =====")

    # Run add book test
    print("\n----- Testing Add Book Functionality -----")
    add_book_result = test_add_book()

    # Run update book test
    print("\n----- Testing Update Book Functionality -----")
    update_book_result = test_update_book()

    # Check if all tests passed
    all_passed = add_book_result and update_book_result

    if all_passed:
        print("\n===== All tests passed! Book management functionality is working correctly. =====")
    else:
        print("\n===== Some tests failed! Book management functionality has issues. =====")

    return all_passed

if __name__ == "__main__":
    import sys

    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        test_mode = sys.argv[1]
        if test_mode == "1":
            test_result = test_add_book()
        elif test_mode == "2":
            test_result = test_update_book()
        else:
            test_result = run_all_tests()
    else:
        # Default to running all tests if no arguments provided
        print("No test mode specified, running all tests...")
        test_result = run_all_tests()

    # Exit with appropriate status code
    sys.exit(0 if test_result else 1)
