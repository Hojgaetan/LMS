from flask import Blueprint, render_template, jsonify
from services.dashboard_service import DashboardService
from models.book import Book
from models.member import Member
from models.category import Category
from models.author import Author

dashboard_blueprint = Blueprint('dashboard', __name__)

dashboard_service = DashboardService(Book, Member, Category, Author)

@dashboard_blueprint.route('/', methods=['GET'])
def dashboard():
    try:
        stats = dashboard_service.get_dashboard_statistics()
        books_data = dashboard_service.get_books_data()
        return render_template('index.html', **stats, books=books_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@dashboard_blueprint.route('/books-data', methods=['GET'])
def get_books_data():
    try:
        books_data = dashboard_service.get_books_data()
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500