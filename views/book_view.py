class BookView:
    """View class for book-related user interface."""

    @staticmethod
    def display_add_book_menu():
        """
        Display the menu for adding a new book.
        """
        print("\n===== Add New Book =====")

    @staticmethod
    def display_authors(authors):
        """
        Display a list of authors.

        Args:
            authors (list): A list of Author objects
        """
        print("\nAvailable Authors:")
        for author in authors:
            print(f"{author.author_id}. {author.name}")

    @staticmethod
    def display_categories(categories):
        """
        Display a list of categories.

        Args:
            categories (list): A list of Category objects
        """
        print("\nAvailable Categories:")
        for category in categories:
            print(f"{category.category_id}. {category.name}")

    @staticmethod
    def get_book_details():
        """
        Get book details from the user.

        Returns:
            dict: A dictionary containing the book details
        """
        print("\nEnter book details:")

        book_details = {}

        # Get required fields
        book_details["title"] = input("Title (required): ")

        try:
            book_details["author_id"] = int(input("Author ID (required): "))
            book_details["category_id"] = int(input("Category ID (required): "))

            # Get optional fields
            isbn = input("ISBN (optional, press Enter to skip): ")
            if isbn:
                book_details["isbn"] = isbn

            pub_year = input("Publication Year (optional, press Enter to skip): ")
            if pub_year:
                book_details["publication_year"] = int(pub_year)

            publisher = input("Publisher (optional, press Enter to skip): ")
            if publisher:
                book_details["publisher"] = publisher

            quantity = input("Quantity (optional, default is 1, press Enter to use default): ")
            if quantity:
                book_details["quantity"] = int(quantity)

            return book_details

        except ValueError:
            print("\nError: Please enter valid numeric values for Author ID, Category ID, Publication Year, and Quantity.")
            return None

    @staticmethod
    def display_book(book):
        """
        Display detailed information about a book.

        Args:
            book (Book): The book to display
        """
        if not book:
            print("Book not found.")
            return

        print("\n===== Book Details =====")
        print(f"ID: {book.book_id}")
        print(f"Title: {book.title}")
        print(f"Author ID: {book.author_id}")
        print(f"Category ID: {book.category_id}")

        if book.isbn:
            print(f"ISBN: {book.isbn}")

        if book.publication_year:
            print(f"Publication Year: {book.publication_year}")

        if book.publisher:
            print(f"Publisher: {book.publisher}")

        print(f"Quantity: {book.quantity}")
        print(f"Available: {book.available_quantity}")

    @staticmethod
    def display_books(books):
        """
        Display a list of books.

        Args:
            books (list): A list of Book objects
        """
        if not books:
            print("No books found matching the criteria.")
            return

        print("\n===== Search Results =====")
        for book in books:
            print(
                f"ID: {book.book_id} | Title: {book.title} | Author ID: {book.author_id} | Category ID: {book.category_id} | ISBN: {book.isbn}"
            )

    @staticmethod
    def display_update_book_menu():
        """
        Display the menu for updating a book.
        """
        print("\n===== Update Book Information =====")

    @staticmethod
    def get_book_id_for_update():
        """
        Get the ID of the book to update.

        Returns:
            int or None: The book ID, or None if the input is invalid
        """
        try:
            book_id = int(input("Enter the ID of the book to update: "))
            return book_id
        except ValueError:
            print("Error: Please enter a valid book ID.")
            return None

    @staticmethod
    def get_book_update_details():
        """
        Get updated book details from the user.

        Returns:
            dict: A dictionary containing the updated book details
        """
        print("\nEnter new book details (press Enter to keep current value):")

        book_updates = {}

        # Get optional fields
        title = input("Title: ")
        if title:
            book_updates["title"] = title

        try:
            author_id = input("Author ID: ")
            if author_id:
                book_updates["author_id"] = int(author_id)

            category_id = input("Category ID: ")
            if category_id:
                book_updates["category_id"] = int(category_id)

            isbn = input("ISBN: ")
            if isbn:
                book_updates["isbn"] = isbn

            pub_year = input("Publication Year: ")
            if pub_year:
                book_updates["publication_year"] = int(pub_year)

            publisher = input("Publisher: ")
            if publisher:
                book_updates["publisher"] = publisher

            quantity = input("Quantity: ")
            if quantity:
                book_updates["quantity"] = int(quantity)

            return book_updates

        except ValueError:
            print("\nError: Please enter valid numeric values for Author ID, Category ID, Publication Year, and Quantity.")
            return None

    @staticmethod
    def remove_book_menu():
        """
        Display the menu for removing a book and handle user input.
        """
        print("\n===== Remove Book =====")
        try:
            book_id = int(input("Enter the Book ID to remove: "))
        except ValueError:
            print("Invalid input. Please enter a valid Book ID.")
            return
        from controllers.book_controller import BookController

        success, message = BookController.remove_book(book_id)
        print(message)

    @staticmethod
    def get_search_criteria():
        """
        Prompt the user for search criteria (title, author ID, category ID, ISBN).
        Returns:
            dict: Dictionary with keys 'title', 'author_id', 'category_id', 'isbn' (values may be None)
        """
        print("\n===== Search Books =====")
        while True:
            title = input("Title (required): ")
            if title:
                break
            print("Error: Title is required. Please enter a title.")
        return {"title": title}
