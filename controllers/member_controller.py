from flask import Blueprint, jsonify
from services.member_service import MemberService

member_blueprint = Blueprint('members', __name__)

@member_blueprint.route('/total-members', methods=['GET'])
def total_members():
    try:
        total_members = MemberService.count_members()
        return jsonify({'total_members': total_members})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@member_blueprint.route('/total-active-members', methods=['GET'])
def total_active_members():
    try:
        total_active_members = MemberService.count_active_members()
        return jsonify({'total_active_members': total_active_members})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@member_blueprint.route('/add', methods=['POST'])
def add_member():
    try:
        data = request.get_json()
        # Vérifier si le membre existe déjà (par email)
        existing_member = MemberService.get_member_by_email(data.get('email'))
        if existing_member:
            return jsonify({'success': False,
                            'message': 'Un membre avec cet email existe déjà.'
                            }), 400
        # Ajouter le nouveau membre
        success, msg = MemberService.add_member(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address'),
            registration_date=data.get('registration_date')
        )
        if success:
            return jsonify({'success': True,
                            'message': msg
                            }), 201
        else:
            return jsonify({'success': False,
                            'message': msg
                            }), 400

    except Exception as e:
        return jsonify(
            {'success': False,
             'message': f'Server error: {str(e)}'
             }), 500

