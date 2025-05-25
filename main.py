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

    def run(self):
        """Run the main application loop."""
        while True:
            # Display the main menu and get user choice
            choice = self.menu_view.display_main_menu()

            if choice == '1':
                self.add_new_book()
            elif choice == '2':
                self.menu_view.display_message("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                self.menu_view.display_error("Invalid choice. Please try again.")

def main():
    """Main entry point for the application."""
    app = LibraryManagementSystem()
    app.run()

if __name__ == "__main__":
    main()
