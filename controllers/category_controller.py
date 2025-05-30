from flask import Blueprint, jsonify
from services.category_service import CategoryService

book_category_blueprint = Blueprint('book_category', __name__)

@book_category_blueprint.route('/total-category', methods=['GET'])
def total_categories():
    try:
        total_category = CategoryService.count_categories()
        return jsonify({'total_category': total_category})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
