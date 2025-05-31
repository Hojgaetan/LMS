from services.book_service import BookService
from services.member_service import MemberService
from services.category_service import CategoryService
from services.author_service import AuthorService

class DashboardService:
    def __init__(self):
        self.book_service = BookService()
        self.member_service = MemberService()
        self.category_service = CategoryService()
        self.author_service = AuthorService()

    def get_dashboard_statistics(self):
        try:
            return {
                'total_books': self.book_service.count_books(),
                'total_category': self.category_service.count_categories(),
                'total_authors': self.author_service.count_authors(),
                'total_members': self.member_service.count_members(),
                'total_popular_books': self.book_service.count_popular_books(threshold=10),
                'total_active_members': self.member_service.count_active_members(),
                'total_overdue_books': self.book_service.count_overdue_books()
            }
        except Exception as e:
            raise Exception(f"Error fetching dashboard statistics: {str(e)}")

    def get_books_data(self):
        try:
            books = self.book_service.get_all_books()
            books_data = []
            for book in books:
                books_data.append({
                    'id': book.book_id,
                    'title': book.title,
                    'author': self.author_service.get_author_name(book.author_id) if book.author_id else '',
                    'category': self.category_service.get_category_name(book.category_id) if book.category_id else '',
                    'isbn': book.isbn,
                    'publication_year': book.publication_year,
                    'publisher': book.publisher,
                    'quantity': book.quantity,
                    'available_quantity': book.available_quantity
                })
            return books_data
        except Exception as e:
            raise Exception(f"Error fetching books data: {str(e)}")

    def get_members_loans_data(self):
        try:
            members = self.member_service.get_all_members_with_loans()
            members_loans_data = []
            for member in members:
                members_loans_data.append({
                    'name': member.name,
                    'email': member.email,
                    'loans_count': len(member.loans),
                    'last_loan_due_date': member.loans[-1].due_date if member.loans else None
                })
            return members_loans_data
        except Exception as e:
            raise Exception(f"Error fetching members loans data: {str(e)}")
        
    def get_overdue_books_data(self):
        try:
            from datetime import datetime
            overdue_books = self.book_service.get_overdue_books()
            overdue_books_data = []
            for book in overdue_books:
                overdue_books_data.append({
                    'title': book.title,
                    'member': book.borrowing.member.name,
                    'borrow_date': book.borrowing.borrow_date,
                    'due_date': book.borrowing.due_date,
                    'days_overdue': (datetime.now() - book.borrowing.due_date).days if datetime.now() > book.borrowing.due_date else 0
                })
            return overdue_books_data
        except Exception as e:
            raise Exception(f"Error fetching overdue books data: {str(e)}")

