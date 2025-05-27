class BorrowingView:
    """View class for borrowing-related user interface."""

    @staticmethod
    def display_borrow_book_menu():
        print("\n===== Borrow Book =====")
        book_id = input("Book ID to borrow: ")
        member_id = input("Member ID: ")
        days = input("Number of days (default 14): ")
        days = int(days) if days.isdigit() else 14
        return book_id, member_id, days

    @staticmethod
    def display_return_book_menu():
        print("\n===== Return Book =====")
        borrowing_id = input("Borrowing ID to return: ")
        return borrowing_id

    @staticmethod
    def display_extend_borrowing_menu():
        print("\n===== Extend Borrowing Period =====")
        borrowing_id = input("Borrowing ID to extend: ")
        extra_days = input("Number of extra days: ")
        return borrowing_id, int(extra_days) if extra_days.isdigit() else 0

    @staticmethod
    def display_overdue_borrowings(overdues):
        print("\n===== Overdue Borrowings =====")
        if not overdues:
            print("No overdue borrowings.")
            return
        for b in overdues:
            print(f"Borrowing ID: {b.borrowing_id} | Book ID: {b.book_id} | Member ID: {b.member_id} | Due: {b.due_date} | Status: {b.status}")

    @staticmethod
    def display_message(message):
        print(message)
