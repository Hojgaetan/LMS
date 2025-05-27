import unittest
from controllers.borrowing_controller import BorrowingController
from controllers.book_controller import BookController
from controllers.member_controller import MemberController
from models.borrowing import Borrowing
from models.book import Book
from models.member import Member

class TestBorrowingController(unittest.TestCase):
    def setUp(self):
        # Clean up test data
        for m in Member.find_by_name("Test Borrower"):
            m.delete()
        for b in Book.find_by_title("Test Borrow Book"):
            Book.delete(b.book_id)
        # Add a test member and book
        MemberController.add_member("Test Borrower", email="borrower@example.com")
        BookController.add_book("Test Borrow Book", author_id=1, category_id=1, quantity=2)
        self.member = Member.find_by_email("borrower@example.com")
        self.book = Book.find_by_title("Test Borrow Book")[0]

    def tearDown(self):
        for m in Member.find_by_name("Test Borrower"):
            m.delete()
        for b in Book.find_by_title("Test Borrow Book"):
            Book.delete(b.book_id)

    def test_borrow_book(self):
        success, msg = BorrowingController.borrow_book(self.book.book_id, self.member.member_id)
        self.assertTrue(success)
        self.assertIn("borrowed by member", msg)
        # Clean up borrowings
        for br in Borrowing.find_by_member(self.member.member_id):
            br.delete()

    def test_return_book(self):
        BorrowingController.borrow_book(self.book.book_id, self.member.member_id)
        borrowings = Borrowing.find_by_member(self.member.member_id)
        self.assertTrue(borrowings)
        borrowing = borrowings[0]
        success, msg = BorrowingController.return_book(borrowing.borrowing_id)
        self.assertTrue(success)
        self.assertIn("returned successfully", msg)
        borrowing.delete()

    def test_extend_borrowing(self):
        BorrowingController.borrow_book(self.book.book_id, self.member.member_id)
        borrowing = Borrowing.find_by_member(self.member.member_id)[0]
        old_due = borrowing.due_date
        success, msg = BorrowingController.extend_borrowing(borrowing.borrowing_id, 7)
        self.assertTrue(success)
        self.assertIn("extended", msg)
        borrowing.delete()

    def test_get_overdue_borrowings(self):
        # This test assumes no overdue borrowings exist
        overdues = BorrowingController.get_overdue_borrowings()
        self.assertIsInstance(overdues, list)

    def test_send_reminder(self):
        BorrowingController.borrow_book(self.book.book_id, self.member.member_id)
        borrowing = Borrowing.find_by_member(self.member.member_id)[0]
        success, msg = BorrowingController.send_reminder(borrowing.borrowing_id)
        self.assertTrue(success)
        self.assertIn("Reminder sent", msg)
        borrowing.delete()

if __name__ == "__main__":
    unittest.main()
