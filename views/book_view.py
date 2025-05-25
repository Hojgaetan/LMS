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
        book_details['title'] = input("Title (required): ")
        
        try:
            book_details['author_id'] = int(input("Author ID (required): "))
            book_details['category_id'] = int(input("Category ID (required): "))
            
            # Get optional fields
            isbn = input("ISBN (optional, press Enter to skip): ")
            if isbn:
                book_details['isbn'] = isbn
            
            pub_year = input("Publication Year (optional, press Enter to skip): ")
            if pub_year:
                book_details['publication_year'] = int(pub_year)
            
            publisher = input("Publisher (optional, press Enter to skip): ")
            if publisher:
                book_details['publisher'] = publisher
            
            quantity = input("Quantity (optional, default is 1, press Enter to use default): ")
            if quantity:
                book_details['quantity'] = int(quantity)
            
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
            print("No books found.")
            return
        
        print("\n===== Books =====")
        for book in books:
            print(f"{book.book_id}. {book.title} (ISBN: {book.isbn or 'N/A'})")