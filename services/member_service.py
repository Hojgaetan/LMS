from models.member import Member


class MemberService:
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
    def get_member(member_id):
        """Retourne un membre par ID ou None."""
        return Member.find_by_id(member_id)

    @staticmethod
    def update_member(member_id, name=None, email=None, phone=None, address=None, status=None):
        try:
            print("Début de la mise à jour du membre:", member_id)  # Log de début
            member = Member.find_by_id(member_id)
            if not member:
                print("Membre non trouvé dans le service")  # Log si le membre n'existe pas
                return False, "Le membre n'a pas été trouvé dans la base de données."

            print(
                "Membre trouvé, données actuelles:",
                {  # Log des données actuelles
                    "name": member.name,
                    "email": member.email,
                    "phone": member.phone,
                    "address": member.address,
                },
            )

            # Mettre à jour les champs si fournis
            if name is not None:
                print("Mise à jour du nom:", name)  # Log de la mise à jour du nom
                member.name = name
            if email is not None:
                print("Mise à jour de l'email:", email)  # Log de la mise à jour de l'email
                member.email = email
            if phone is not None:
                print("Mise à jour du téléphone:", phone)  # Log de la mise à jour du téléphone
                member.phone = phone
            if address is not None:
                print("Mise à jour de l'adresse:", address)  # Log de la mise à jour de l'adresse
                member.address = address
            if status is not None:
                print("Mise à jour du statut:", status)  # Log de la mise à jour du statut
                member.status = status

            print("Validation des données")  # Log avant validation
            # Valider les données
            valid, msg = member.validate()
            if not valid:
                print("Erreur de validation:", msg)  # Log de l'erreur de validation
                return False, msg

            print("Sauvegarde des modifications")  # Log avant sauvegarde
            # Sauvegarder les modifications
            member.save()
            print("Mise à jour réussie")  # Log de succès
            return True, f"Les informations du membre ont été mises à jour avec succès."

        except Exception as e:
            print("Erreur dans update_member:", str(e))  # Log de l'erreur
            import traceback

            print("Traceback complet:", traceback.format_exc())  # Log du traceback complet
            return False, f"Une erreur est survenue lors de la mise à jour : {str(e)}"

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

    def get_members_loans_data(self):
        try:
            members = self.member_model.get_all_members_with_loans()
            members_loans_data = []
            for member in members:
                members_loans_data.append(
                    {
                        "name": member.name,
                        "email": member.email,
                        "loans_count": len(member.loans),
                        "last_loan_due_date": member.loans[-1].due_date if member.loans else None,
                    }
                )
            return members_loans_data
        except Exception as e:
            raise Exception(f"Error fetching members loans data: {str(e)}")

    @staticmethod
    def count_members():
        """Count the total number of members."""
        return Member.count()

    @staticmethod
    def count_active_members():
        """Count the total number of active members based on recent loans."""
        return Member.count_active_members()

    @staticmethod
    def get_all_members_with_loans():
        """
        Retrieve all members along with their loan information.

        Returns:
            list: A list of Member objects with their loans populated.
        """
        members = Member.find_all()
        for member in members:
            member.loans = member.get_borrowings()
        return members

    @staticmethod
    def get_member_by_email(email):
        """Return a member object if a member with the given email exists, else None."""
        return Member.find_by_email(email)

    @staticmethod
    def get_all_members():
        """Return a list of all members."""
        return Member.find_all()
