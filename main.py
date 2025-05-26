import asyncio
from controllers.database_controller import DatabaseController
from controllers.book_controller import BookController
from views.menu_view import MenuView
from views.book_view import BookView

"""
some notes:

     probably will be usefull : https://github.com/internetarchive/openlibrary-client







"""


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

    async def add_new_book(self):
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
        book_details = await self.book_view.get_book_details()

        if book_details:
            # Add the book to the database
            success, result = self.book_controller.add_book(**book_details)

            if success:
                self.menu_view.display_success(f"Book added successfully with ID: {result}")
            else:
                self.menu_view.display_error(result)

    async def update_book(self):
        """Handle the update book functionality."""
        # Display the update book menu
        self.book_view.display_update_book_menu()

        # Get the book ID from user
        book_id = await self.book_view.get_book_id_for_update()

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
        book_updates = await self.book_view.get_book_update_details()

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

    async def run(self):
        """Run the main application loop."""

        self.menu_view.clear()
        self.menu_view.goto_xy(5, 10)

        while True:
            # Display the main menu and get user choice
            choice = await self.menu_view.display_main_menu()

            if choice == "1":
                await self.add_new_book()
            elif choice == "2":
                await self.update_book()
            elif choice == "3":
                await self.remove_book()
            elif choice == "4":
                break
            else:
                self.menu_view.display_error("Invalid choice. Please try again.")
            await asyncio.sleep(0)

        # exit
        self.menu_view.display_message("Thank you for using the Library Management System. Goodbye!")


async def main():
    """Main entry point for the application."""
    await LibraryManagementSystem().run()


if __name__ == "__main__":
    asyncio.run(main())
