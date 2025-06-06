from flask import Blueprint, jsonify, request
from services.member_service import MemberService
from models.member import Member
from datetime import datetime

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
                            'message': 'Member with this email already exist.'
                            }), 400
        # Ajouter le nouveau membre avec la date d'inscription actuelle
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M")

        success, msg = MemberService.add_member(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address'),
            registration_date=current_date
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

@member_blueprint.route('/update', methods=['POST'])
def update_member():
    try:
        data = request.get_json()

        member_id = data.get('member_id')

        # Vérifier si le membre existe
        member = Member.find_by_id(member_id)
        if not member:
            return jsonify({
                'success': False,
                'message': 'Le membre que vous essayez de modifier n\'existe pas dans la base de données.'
            }), 404

        # Vérifier si l'email est déjà utilisé par un autre membre (uniquement si l'email a changé)
        if data.get('email') and data.get('email') != member.email:
            existing_member = MemberService.get_member_by_email(data.get('email'))
            if existing_member and existing_member.member_id != member_id:
                print("Email déjà utilisé")
                return jsonify({
                    'success': False,
                    'message': 'Cette adresse email est déjà utilisée par un autre membre de la bibliothèque.'
                }), 400

        # Vérifier que tous les champs requis sont présents
        required_fields = ['name', 'email', 'phone', 'address']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            print("Champs manquants:", missing_fields)
            return jsonify({
                'success': False,
                'message': f'Veuillez remplir tous les champs obligatoires : {", ".join(missing_fields)}'
            }), 400

        print("Tentative de mise à jour du membre")
        # Mettre à jour le membre
        success, msg = MemberService.update_member(
            member_id=member_id,
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address')
        )
        print("Résultat de la mise à jour:", success, msg)

        if success:
            return jsonify({
                'success': True,
                'message': f'Les informations de {data.get("name")} ont été mises à jour avec succès.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': msg
            }), 400

    except Exception as e:
        #print("Erreur détaillée:", str(e))
        #import traceback
        #print("Traceback complet:", traceback.format_exc())
        return jsonify({
            'success': False,
            'message': 'Une erreur inattendue est survenue lors de la modification des informations du membre.'
        }), 500

@member_blueprint.route('/delete', methods=['POST'])
def delete_member():
    try:
        data = request.get_json()
        if not data or 'member_id' not in data:
            return jsonify({
                'success': False,
                'message': 'ID du membre manquant dans la requête'
            }), 400

        member_id = data.get('member_id')
        if not isinstance(member_id, (int, str)) or not str(member_id).isdigit():
            return jsonify({
                'success': False,
                'message': 'ID du membre invalide'
            }), 400

        member_id = int(member_id)

        # Vérifier si le membre existe
        member = Member.find_by_id(member_id)
        if not member:
            return jsonify({
                'success': False,
                'message': f'Membre avec ID {member_id} non trouvé'
            }), 404

        # Vérifier si le membre a des emprunts en cours
        borrowings = MemberService.get_member_history(member_id)
        active_borrowings = [b for b in borrowings if b.status == "borrowed"]
        if active_borrowings:
            return jsonify({
                'success': False,
                'message': 'Impossible de supprimer ce membre car il a des emprunts en cours'
            }), 400

        # Supprimer le membre
        success, msg = MemberService.delete_member(member_id)
        if success:
            return jsonify({
                'success': True,
                'message': msg
            }), 200

        else:
            return jsonify({
                'success': False,
                'message': msg
            }), 400

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erreur serveur: {str(e)}'
        }), 500

