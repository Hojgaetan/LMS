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

    def add_new_category(self):
        """Handle the add new category functionality."""
        from controllers.category_controller import CategoryController
        from views.category_view import CategoryView

        name, description = CategoryView.display_add_category_menu()
        success, message = CategoryController.add_category(name, description)
        CategoryView.display_message(message)

    def update_category(self):
        """Handle the update category functionality."""
        from controllers.category_controller import CategoryController
        from views.category_view import CategoryView

        category_id, name, description = CategoryView.display_update_category_menu()
        if not category_id.isdigit():
            CategoryView.display_message("Invalid category ID.")
            return
        success, message = CategoryController.update_category(int(category_id), name or None, description or None)
        CategoryView.display_message(message)

    def delete_category(self):
        """Handle the delete category functionality."""
        from controllers.category_controller import CategoryController
        from views.category_view import CategoryView

        category_id = CategoryView.display_delete_category_menu()
        if not category_id.isdigit():
            CategoryView.display_message("Invalid category ID.")
            return
        success, message = CategoryController.delete_category(int(category_id))
        CategoryView.display_message(message)

    def list_categories(self):
        """Handle the list categories functionality."""
        from controllers.category_controller import CategoryController
        from views.category_view import CategoryView

        categories = CategoryController.list_categories()
        CategoryView.display_categories(categories)

    def search_categories(self):
        """Handle the search categories functionality."""
        from controllers.category_controller import CategoryController
        from views.category_view import CategoryView

        name = CategoryView.display_search_category_menu()
        categories = CategoryController.search_categories_by_name(name)
        CategoryView.display_categories(categories)

    def add_new_member(self):
        """Handle the add new member functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        name, email, phone, address = MemberView.display_add_member_menu()
        success, message = MemberController.add_member(name, email, phone, address)
        MemberView.display_message(message)

    def update_member(self):
        """Handle the update member functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        member_id, name, email, phone, address, status = MemberView.display_update_member_menu()
        if not member_id.isdigit():
            MemberView.display_message("Invalid member ID.")
            return
        success, message = MemberController.update_member(int(member_id), name or None, email or None, phone or None, address or None, status or None)
        MemberView.display_message(message)

    def delete_member(self):
        """Handle the delete member functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        member_id = MemberView.display_delete_member_menu()
        if not member_id.isdigit():
            MemberView.display_message("Invalid member ID.")
            return
        success, message = MemberController.delete_member(int(member_id))
        MemberView.display_message(message)

    def list_members(self):
        """Handle the list members functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        members = MemberController.list_members()
        MemberView.display_members(members)

    def search_members(self):
        """Handle the search members functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        name = MemberView.display_search_member_menu()
        members = MemberController.search_members_by_name(name)
        MemberView.display_members(members)

    def view_member_history(self):
        """Handle the view member history functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        member_id = input("Enter Member ID to view history: ")
        if not member_id.isdigit():
            MemberView.display_message("Invalid member ID.")
            return
        history = MemberController.get_member_history(int(member_id))
        MemberView.display_member_history(history)

    def set_member_status(self):
        """Handle the set member status functionality."""
        from controllers.member_controller import MemberController
        from views.member_view import MemberView
        member_id = input("Enter Member ID to change status: ")
        if not member_id.isdigit():
            MemberView.display_message("Invalid member ID.")
            return
        status = input("Enter new status (active/inactive): ")
        success, message = MemberController.set_member_status(int(member_id), status)
        MemberView.display_message(message)

    def borrow_book(self):
        from controllers.borrowing_controller import BorrowingController
        from views.borrowing_view import BorrowingView
        book_id, member_id, days = BorrowingView.display_borrow_book_menu()
        if not book_id.isdigit() or not member_id.isdigit():
            BorrowingView.display_message("Invalid book or member ID.")
            return
        success, message = BorrowingController.borrow_book(int(book_id), int(member_id), days)
        BorrowingView.display_message(message)

    def return_book(self):
        from controllers.borrowing_controller import BorrowingController
        from views.borrowing_view import BorrowingView
        borrowing_id = BorrowingView.display_return_book_menu()
        if not borrowing_id.isdigit():
            BorrowingView.display_message("Invalid borrowing ID.")
            return
        success, message = BorrowingController.return_book(int(borrowing_id))
        BorrowingView.display_message(message)

    def extend_borrowing(self):
        from controllers.borrowing_controller import BorrowingController
        from views.borrowing_view import BorrowingView
        borrowing_id, extra_days = BorrowingView.display_extend_borrowing_menu()
        if not borrowing_id.isdigit() or extra_days <= 0:
            BorrowingView.display_message("Invalid input.")
            return
        success, message = BorrowingController.extend_borrowing(int(borrowing_id), extra_days)
        BorrowingView.display_message(message)

    def show_overdue_borrowings(self):
        from controllers.borrowing_controller import BorrowingController
        from views.borrowing_view import BorrowingView
        overdues = BorrowingController.get_overdue_borrowings()
        BorrowingView.display_overdue_borrowings(overdues)

    def send_borrowing_reminder(self):
        from controllers.borrowing_controller import BorrowingController
        from views.borrowing_view import BorrowingView
        borrowing_id = input("Enter Borrowing ID to send reminder: ")
        if not borrowing_id.isdigit():
            BorrowingView.display_message("Invalid borrowing ID.")
            return
        success, message = BorrowingController.send_reminder(int(borrowing_id))
        BorrowingView.display_message(message)

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
                    self.add_new_category()
                elif choice == "11":
                    self.update_category()
                elif choice == "12":
                    self.delete_category()
                elif choice == "13":
                    self.list_categories()
                elif choice == "14":
                    self.search_categories()
                elif choice == "15":
                    self.add_new_member()
                elif choice == "16":
                    self.update_member()
                elif choice == "17":
                    self.delete_member()
                elif choice == "18":
                    self.list_members()
                elif choice == "19":
                    self.search_members()
                elif choice == "20":
                    self.view_member_history()
                elif choice == "21":
                    self.set_member_status()
                elif choice == "22":
                    self.borrow_book()
                elif choice == "23":
                    self.return_book()
                elif choice == "24":
                    self.extend_borrowing()
                elif choice == "25":
                    self.show_overdue_borrowings()
                elif choice == "26":
                    self.send_borrowing_reminder()
                elif choice == "27":
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
