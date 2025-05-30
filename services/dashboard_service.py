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

    def get_books_data(self):
        try:
            books = self.book_model.get_all_books()
            books_data = []
            for book in books:
                books_data.append({
                    'id': book.book_id,
                    'title': book.title,
                    'author': self.author_model.find_by_id(book.author_id).name if book.author_id else '',
                    'category': self.category_model.find_by_id(book.category_id).name if book.category_id else '',
                    'isbn': book.isbn,
                    'publication_year': book.publication_year,
                    'publisher': book.publisher,
                    'quantity': book.quantity,
                    'available_quantity': book.available_quantity
                })
            return books_data
        except Exception as e:
            raise Exception(f"Error fetching books data: {str(e)}")
