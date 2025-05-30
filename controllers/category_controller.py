from flask import Blueprint, jsonify, request
from models.book import Book

book_category_blueprint = Blueprint('book_category', __name__)

@book_category_blueprint.route('/total-category', methods=['GET'])
def total_categories():
    try:
        total_category = Book.count()
        return jsonify({'total_category': total_category})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
