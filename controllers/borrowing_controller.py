from services.borrowing_service import BorrowingService
from services.book_service import BookService
from services.member_service import MemberService
from datetime import datetime, timedelta


class BorrowingController:
    """Controller for borrowing-related operations."""

    @staticmethod
    def borrow_book(book_id, member_id, days=14):
        book = BookService.get_book(book_id)
        member = MemberService.get_member(member_id)
        if not book:
            return False, "Book not found."
        if not member:
            return False, "Member not found."
        if getattr(book, "available_quantity", 0) < 1:
            return False, "No available copies for this book."
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        success, message = BorrowingService.create_borrowing(book_id, member_id, borrow_date, due_date)
        if success:
            BookService.update_book(book_id, available_quantity=book.available_quantity - 1)
            return True, f"Book '{book.title}' borrowed by member '{member.name}'. Due date: {due_date}."
        return False, message

    @staticmethod
    def return_book(borrowing_id):
        borrowing = BorrowingService.get_borrowing(borrowing_id)
        if not borrowing:
            return False, "Borrowing record not found."
        if borrowing.status == "returned":
            return False, "Book already returned."
        return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success, message = BorrowingService.update_borrowing(borrowing_id, status="returned", return_date=return_date)
        if success:
            book = BookService.get_book(borrowing.book_id)
            if book:
                BookService.update_book(book.book_id, available_quantity=book.available_quantity + 1)
            return True, "Book returned successfully."
        return False, message

    @staticmethod
    def extend_borrowing(borrowing_id, extra_days):
        borrowing = BorrowingService.get_borrowing(borrowing_id)
        if not borrowing:
            return False, "Borrowing record not found."
        if borrowing.status == "returned":
            return False, "Cannot extend a returned book."
        due_date = datetime.strptime(borrowing.due_date, "%Y-%m-%d %H:%M:%S")
        new_due_date = (due_date + timedelta(days=extra_days)).strftime("%Y-%m-%d %H:%M:%S")
        success, message = BorrowingService.update_borrowing(borrowing_id, due_date=new_due_date)
        if success:
            return True, f"Borrowing period extended. New due date: {new_due_date}."
        return False, message

    @staticmethod
    def get_overdue_borrowings():
        return BorrowingService.get_overdue_borrowings()

    @staticmethod
    def send_reminder(borrowing_id):
        borrowing = BorrowingService.get_borrowing(borrowing_id)
        if not borrowing:
            return False, "Borrowing record not found."
        member = MemberService.get_member(borrowing.member_id)
        if not member:
            return False, "Member not found."
        return (
            True,
            f"Reminder sent to {member.name} (Email: {member.email}) for book ID {borrowing.book_id}. Due date: {borrowing.due_date}.",
        )
