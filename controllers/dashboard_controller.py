from flask import Blueprint, render_template, jsonify
from services.dashboard_service import DashboardService

dashboard_blueprint = Blueprint('dashboard', __name__)

dashboard_service = DashboardService()

@dashboard_blueprint.route('/', methods=['GET'])
def dashboard():
    try:
        stats = dashboard_service.get_dashboard_statistics()
        books_data = dashboard_service.get_books_data()
        members_loans_data = dashboard_service.get_members_loans_data()
        return render_template('index.html', **stats, books=books_data, members_loans=members_loans_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@dashboard_blueprint.route('/books-data', methods=['GET'])
def get_books_data():
    try:
        books_data = dashboard_service.get_books_data()
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@dashboard_blueprint.route('/members-loans', methods=['GET'])
def get_members_loans():
    try:
        members_loans_data = dashboard_service.get_members_loans_data()
        return jsonify({'members_loans': members_loans_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500