from models.borrowing import Borrowing
from models.book import Book
from models.member import Member
from utils.db_utils import DatabaseConnection
from datetime import datetime, timedelta


class BorrowingService:
    """Controller for borrowing-related operations."""

    @staticmethod
    def borrow_book(book_id, member_id, days=14):
        book = Book.find_by_id(book_id)
        member = Member.find_by_id(member_id)
        if not book:
            return False, "Book not found."
        if not member:
            return False, "Member not found."
        if getattr(book, "available_quantity", 0) < 1:
            return False, "No available copies for this book."
        borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
        borrowing = Borrowing(book_id=book_id, member_id=member_id, borrow_date=borrow_date, due_date=due_date, status="borrowed")
        borrowing.save()
        book.available_quantity -= 1
        book.save()
        return True, f"Book '{book.title}' borrowed by member '{member.name}'. Due date: {due_date}."

    @staticmethod
    def return_book(borrowing_id):
        borrowing = Borrowing.find_by_id(borrowing_id)
        if not borrowing:
            return False, "Borrowing record not found."
        if borrowing.status == "returned":
            return False, "Book already returned."
        borrowing.return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        borrowing.status = "returned"
        borrowing.save()
        book = Book.find_by_id(borrowing.book_id)
        if book:
            book.available_quantity += 1
            book.save()
        return True, "Book returned successfully."

    @staticmethod
    def extend_borrowing(borrowing_id, extra_days):
        borrowing = Borrowing.find_by_id(borrowing_id)
        if not borrowing:
            return False, "Borrowing record not found."
        if borrowing.status == "returned":
            return False, "Cannot extend a returned book."
        due_date = datetime.strptime(borrowing.due_date, "%Y-%m-%d %H:%M:%S")
        new_due_date = (due_date + timedelta(days=extra_days)).strftime("%Y-%m-%d %H:%M:%S")
        borrowing.due_date = new_due_date
        borrowing.save()
        return True, f"Borrowing period extended. New due date: {new_due_date}."

    @staticmethod
    def get_overdue_borrowings():
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Borrowing.find_overdue()

    @staticmethod
    def send_reminder(borrowing_id):
        borrowing = Borrowing.find_by_id(borrowing_id)
        if not borrowing:
            return False, "Borrowing record not found."
        member = Member.find_by_id(borrowing.member_id)
        if not member:
            return False, "Member not found."
        # In a real system, send an email or SMS. Here, just return a message.
        return (
            True,
            f"Reminder sent to {member.name} (Email: {member.email}) for book ID {borrowing.book_id}. Due date: {borrowing.due_date}.",
        )
