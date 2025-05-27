from models.member import Member
from utils.db_utils import DatabaseConnection

class MemberController:
    """Controller for member-related operations."""

    @staticmethod
    def add_member(name, email=None, phone=None, address=None, registration_date=None, status="active"):
        member = Member(name=name, email=email, phone=phone, address=address, registration_date=registration_date, status=status)
        valid, msg = member.validate()
        if not valid:
            return False, msg
        member.save()
        return True, f"Member '{name}' added successfully."

    @staticmethod
    def update_member(member_id, name=None, email=None, phone=None, address=None, status=None):
        member = Member.find_by_id(member_id)
        if not member:
            return False, "Member not found."
        if name:
            member.name = name
        if email:
            member.email = email
        if phone:
            member.phone = phone
        if address:
            member.address = address
        if status:
            member.status = status
        valid, msg = member.validate()
        if not valid:
            return False, msg
        member.save()
        return True, f"Member '{member_id}' updated successfully."

    @staticmethod
    def delete_member(member_id):
        member = Member.find_by_id(member_id)
        if not member:
            return False, "Member not found."
        member.delete()
        return True, f"Member '{member_id}' deleted successfully."

    @staticmethod
    def list_members():
        return Member.find_all()

    @staticmethod
    def search_members_by_name(name):
        return Member.find_by_name(name)

    @staticmethod
    def get_member_history(member_id):
        member = Member.find_by_id(member_id)
        if not member:
            return []
        return member.get_borrowings()

    @staticmethod
    def set_member_status(member_id, status):
        member = Member.find_by_id(member_id)
        if not member:
            return False, "Member not found."
        member.status = status
        member.save()
        return True, f"Member '{member_id}' status updated to {status}."
