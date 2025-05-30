from models.member import Member
from utils.db_utils import DatabaseConnection
from flask import Blueprint, jsonify


member_blueprint = Blueprint('members', __name__)

@member_blueprint.route('/total-members', methods=['GET'])
def total_members():
    try:
        total_members = Member.count()
        return jsonify({'total_members': total_members})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@member_blueprint.route('/total-active-members', methods=['GET'])
def total_active_members():
    try:
        total_active_members = Member.count_active_members()
        return jsonify({'total_active_members': total_active_members})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
