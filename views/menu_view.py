class MenuView:
    """View class for displaying menus and handling user input."""

    @staticmethod
    def display_main_menu():
        """
        Display the main menu of the Library Management System.

        Returns:
            str: The user's choice
        """
        print("\n===== Library Management System =====")
        print("1. Add New Book")
        print("2. Update Book Information")
        print("3. Remove Book")
        print("4. Search Books")
        print("5. Add New Author")
        print("6. Update Author")
        print("7. Delete Author")
        print("8. List Authors")
        print("9. Search Authors")
        print("10. Add New Category")
        print("11. Update Category")
        print("12. Delete Category")
        print("13. List Categories")
        print("14. Search Categories")
        print("15. Register New Member")
        print("16. Update Member Information")
        print("17. Delete Member")
        print("18. List Members")
        print("19. Search Members")
        print("20. View Member History")
        print("21. Activate/Deactivate Member")
        print("22. Borrow Book")
        print("23. Return Book")
        print("24. Extend Borrowing Period")
        print("25. Show Overdue Borrowings")
        print("26. Send Borrowing Reminder")
        print("27. Admin Login")
        print("28. System Configuration")
        print("29. Backup Database")
        print("30. Restore Database")
        print("31. Exit")
        return input("Enter your choice (1-31): ")

    @staticmethod
    def display_message(message):
        """
        Display a message to the user.

        Args:
            message (str): The message to display
        """
        print(message)

    @staticmethod
    def display_error(error):
        """
        Display an error message to the user.

        Args:
            error (str): The error message to display
        """
        print(f"Error: {error}")

    @staticmethod
    def display_success(message):
        """
        Display a success message to the user.

        Args:
            message (str): The success message to display
        """
        print(f"Success: {message}")

    @staticmethod
    def get_input(prompt):
        """
        Get input from the user with a prompt.

        Args:
            prompt (str): The prompt to display

        Returns:
            str: The user's input
        """
        return input(prompt)

    @staticmethod
    def get_int_input(prompt, default=None):
        """
        Get integer input from the user with a prompt.

        Args:
            prompt (str): The prompt to display
            default (int, optional): The default value to use if the user enters nothing

        Returns:
            int or None: The user's input as an integer, or None if the input is invalid
        """
        try:
            value = input(prompt)
            if value == "" and default is not None:
                return default
            return int(value)
        except ValueError:
            return None
