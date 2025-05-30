from flask import Blueprint, jsonify
from services.author_service import AuthorService

author_blueprint = Blueprint('authors', __name__)

@author_blueprint.route('/total-authors', methods=['GET'])
def total_authors():
    try:
        total_authors = AuthorService.count_authors()
        return jsonify({'total_authors': total_authors})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
