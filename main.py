from controllers.database_controller import DatabaseController
from controllers.book_controller import BookController
from views.menu_view import MenuView
from views.book_view import BookView


class LibraryManagementSystem:
    """Main application class for the Library Management System."""

    def __init__(self):
        """Initialize the Library Management System."""
        # Initialize the database
        DatabaseController.initialize_database()

        # Initialize controllers
        self.book_controller = BookController()

        # Initialize views
        self.menu_view = MenuView()
        self.book_view = BookView()

    def add_new_book(self):
        """Handle the add new book functionality."""
        # Display the add book menu
        self.book_view.display_add_book_menu()

        # Get all authors and display them
        authors = self.book_controller.get_all_authors()
        self.book_view.display_authors(authors)

        # Get all categories and display them
        categories = self.book_controller.get_all_categories()
        self.book_view.display_categories(categories)

        # Get book details from user
        book_details = self.book_view.get_book_details()

        if book_details:
            # Add the book to the database
            success, result = self.book_controller.add_book(**book_details)

            if success:
                self.menu_view.display_success(f"Book added successfully with ID: {result}")
            else:
                self.menu_view.display_error(result)

    def update_book(self):
        """Handle the update book functionality."""
        # Display the update book menu
        self.book_view.display_update_book_menu()

        # Get the book ID from user
        book_id = self.book_view.get_book_id_for_update()

        if book_id is None:
            return

        # Get the book from the database
        book = self.book_controller.get_book(book_id)

        if not book:
            self.menu_view.display_error(f"Book with ID {book_id} not found")
            return

        # Display current book details
        self.book_view.display_book(book)

        # Get all authors and display them
        authors = self.book_controller.get_all_authors()
        self.book_view.display_authors(authors)

        # Get all categories and display them
        categories = self.book_controller.get_all_categories()
        self.book_view.display_categories(categories)

        # Get updated book details from user
        book_updates = self.book_view.get_book_update_details()

        if book_updates:
            # Update the book in the database
            success, result = self.book_controller.update_book(book_id, **book_updates)

            if success:
                self.menu_view.display_success(f"Book updated successfully with ID: {result}")
            else:
                self.menu_view.display_error(result)

    def remove_book(self):
        """Handle the remove book functionality."""
        self.book_view.remove_book_menu()

    def search_books(self):
        """Handle the search books functionality."""
        criteria = self.book_view.get_search_criteria()
        books = self.book_controller.search_books(**criteria)
        self.book_view.display_books(books)

    def add_new_author(self):
        """Handle the add new author functionality."""
        from controllers.author_controller import AuthorController
        from views.author_view import AuthorView
        name, biography = AuthorView.display_add_author_menu()
        success, message = AuthorController.add_author(name, biography)
        AuthorView.display_message(message)

    def update_author(self):
        """Handle the update author functionality."""
        from controllers.author_controller import AuthorController
        from views.author_view import AuthorView
        author_id, name, biography = AuthorView.display_update_author_menu()
        if not author_id.isdigit():
            AuthorView.display_message("Invalid author ID.")
            return
        success, message = AuthorController.update_author(int(author_id), name or None, biography or None)
        AuthorView.display_message(message)

    def delete_author(self):
        """Handle the delete author functionality."""
        from controllers.author_controller import AuthorController
        from views.author_view import AuthorView
        author_id = AuthorView.display_delete_author_menu()
        if not author_id.isdigit():
            AuthorView.display_message("Invalid author ID.")
            return
        success, message = AuthorController.delete_author(int(author_id))
        AuthorView.display_message(message)

    def list_authors(self):
        """Handle the list authors functionality."""
        from controllers.author_controller import AuthorController
        from views.author_view import AuthorView
        authors = AuthorController.list_authors()
        AuthorView.display_authors(authors)

    def search_authors(self):
        """Handle the search authors functionality."""
        from controllers.author_controller import AuthorController
        from views.author_view import AuthorView
        name = AuthorView.display_search_author_menu()
        authors = AuthorController.search_authors_by_name(name)
        AuthorView.display_authors(authors)

    def run(self):
        """Run the main application loop with exception handling."""
        while True:
            try:
                # Display the main menu and get user choice
                choice = self.menu_view.display_main_menu()

                if choice == "1":
                    self.add_new_book()
                elif choice == "2":
                    self.update_book()
                elif choice == "3":
                    self.remove_book()
                elif choice == "4":
                    self.search_books()
                elif choice == "5":
                    self.add_new_author()
                elif choice == "6":
                    self.update_author()
                elif choice == "7":
                    self.delete_author()
                elif choice == "8":
                    self.list_authors()
                elif choice == "9":
                    self.search_authors()
                elif choice == "10":
                    self.menu_view.display_message("Thank you for using the Library Management System. Goodbye!")
                    break
                else:
                    self.menu_view.display_error("Invalid choice. Please try again.")
            except Exception as e:
                self.menu_view.display_error(f"An unexpected error occurred: {e}")


def main():
    """Main entry point for the application with global exception handling."""
    try:
        app = LibraryManagementSystem()
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")


if __name__ == "__main__":
    main()
