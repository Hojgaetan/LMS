from flask import Blueprint, jsonify
from models.author import Author
from utils.db_utils import DatabaseConnection

author_blueprint = Blueprint('authors', __name__)

@author_blueprint.route('/total-authors', methods=['GET'])
def total_authors():
    try:
        total_authors = Author.count()
        return jsonify({'total_authors': total_authors})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
