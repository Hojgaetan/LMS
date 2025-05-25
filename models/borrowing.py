from models.base_model import BaseModel
from utils.db_utils import DatabaseConnection
from datetime import datetime, timedelta

class Borrowing(BaseModel):
    """Model class for book borrowings."""

    TABLE_NAME = 'borrowings'
    PRIMARY_KEY = 'borrowing_id'

    def __init__(self, borrowing_id=None, book_id=None, member_id=None, 
                 borrow_date=None, due_date=None, return_date=None, 
                 status='borrowed', **kwargs):
        """Initialize a Borrowing instance."""
        super().__init__(**kwargs)
        self.borrowing_id = borrowing_id
        self.book_id = book_id
        self.member_id = member_id

        # Set borrow date with default value if not provided
        borrow_date = borrow_date or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.borrow_date = borrow_date

        # Calculate due date if not provided
        if not due_date:
            borrow_datetime = datetime.strptime(self.borrow_date, '%Y-%m-%d %H:%M:%S')
            due_datetime = borrow_datetime + timedelta(days=14)
            due_date = due_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.due_date = due_date

        self.return_date = return_date
        self.status = status

    @property
    def borrowing_id(self):
        """Get the borrowing ID."""
        return self._get_attribute('borrowing_id')

    @borrowing_id.setter
    def borrowing_id(self, value):
        """Set the borrowing ID."""
        self._set_attribute('borrowing_id', value)

    @property
    def book_id(self):
        """Get the book ID."""
        return self._get_attribute('book_id')

    @book_id.setter
    def book_id(self, value):
        """Set the book ID."""
        self._set_attribute('book_id', value)

    @property
    def member_id(self):
        """Get the member ID."""
        return self._get_attribute('member_id')

    @member_id.setter
    def member_id(self, value):
        """Set the member ID."""
        self._set_attribute('member_id', value)

    @property
    def borrow_date(self):
        """Get the borrow date."""
        return self._get_attribute('borrow_date')

    @borrow_date.setter
    def borrow_date(self, value):
        """Set the borrow date."""
        self._set_attribute('borrow_date', value)

    @property
    def due_date(self):
        """Get the due date."""
        return self._get_attribute('due_date')

    @due_date.setter
    def due_date(self, value):
        """Set the due date."""
        self._set_attribute('due_date', value)

    @property
    def return_date(self):
        """Get the return date."""
        return self._get_attribute('return_date')

    @return_date.setter
    def return_date(self, value):
        """Set the return date."""
        self._set_attribute('return_date', value)

    @property
    def status(self):
        """Get the borrowing status."""
        return self._get_attribute('status')

    @status.setter
    def status(self, value):
        """Set the borrowing status."""
        self._set_attribute('status', value)

    @classmethod
    def find_by_book(cls, book_id):
        """Find borrowings by book ID."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE book_id = ?"
        results = DatabaseConnection.execute_query(query, (book_id,))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    @classmethod
    def find_by_member(cls, member_id):
        """Find borrowings by member ID."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE member_id = ?"
        results = DatabaseConnection.execute_query(query, (member_id,))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    @classmethod
    def find_overdue(cls):
        """Find all overdue borrowings."""
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE due_date < ? AND return_date IS NULL"
        results = DatabaseConnection.execute_query(query, (current_date,))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    def get_book(self):
        """Get the book associated with this borrowing."""
        from models.book import Book
        return Book.find_by_id(self.book_id)

    def get_member(self):
        """Get the member associated with this borrowing."""
        from models.member import Member
        return Member.find_by_id(self.member_id)

    def return_book(self):
        """Mark the book as returned."""
        if self.status == 'returned':
            return False, "Book already returned"

        self.return_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status = 'returned'

        # Update the book's available quantity
        book = self.get_book()
        if book:
            book.available_quantity += 1
            book.save()

        self.save()
        return True, "Book returned successfully"

    def validate(self):
        """Validate the borrowing data."""
        if not self.book_id:
            return False, "Book ID is required"

        if not self.member_id:
            return False, "Member ID is required"

        # Check if book exists
        from models.book import Book
        book = Book.find_by_id(self.book_id)
        if not book:
            return False, f"Book with ID {self.book_id} does not exist"

        # Check if book is available
        if not self.borrowing_id and book.available_quantity <= 0:
            return False, f"Book '{book.title}' is not available for borrowing"

        # Check if member exists
        from models.member import Member
        member = Member.find_by_id(self.member_id)
        if not member:
            return False, f"Member with ID {self.member_id} does not exist"

        return True, "Borrowing is valid"
