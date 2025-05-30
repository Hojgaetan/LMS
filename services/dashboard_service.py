from models.book import Book
from models.member import Member
from models.category import Category
from models.author import Author

class DashboardService:
    def __init__(self, book_model, member_model, category_model, author_model):
        self.book_model = book_model
        self.member_model = member_model
        self.category_model = category_model
        self.author_model = author_model

    def get_dashboard_statistics(self):
        try:
            return {
                'total_books': self.book_model.count(),
                'total_category': self.category_model.count(),
                'total_authors': self.author_model.count(),
                'total_members': self.member_model.count(),
                'total_popular_books': self.book_model.count_popular_books(threshold=10),
                'total_active_members': self.member_model.count_active_members(),
                'total_overdue_books': self.book_model.count_overdue_books()
            }
        except Exception as e:
            raise Exception(f"Error fetching dashboard statistics: {str(e)}")
