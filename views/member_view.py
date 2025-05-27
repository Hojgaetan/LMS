class MemberView:
    """View class for member-related user interface."""

    @staticmethod
    def display_add_member_menu():
        print("\n===== Register New Member =====")
        name = input("Name (required): ")
        email = input("Email (optional): ")
        phone = input("Phone (optional): ")
        address = input("Address (optional): ")
        return name, email, phone, address

    @staticmethod
    def display_update_member_menu():
        print("\n===== Update Member Information =====")
        member_id = input("Member ID to update: ")
        name = input("New Name (press Enter to skip): ")
        email = input("New Email (press Enter to skip): ")
        phone = input("New Phone (press Enter to skip): ")
        address = input("New Address (press Enter to skip): ")
        status = input("New Status (active/inactive, press Enter to skip): ")
        return member_id, name, email, phone, address, status

    @staticmethod
    def display_delete_member_menu():
        print("\n===== Delete Member =====")
        member_id = input("Member ID to delete: ")
        return member_id

    @staticmethod
    def display_members(members):
        print("\n===== Members List =====")
        if not members:
            print("No members found.")
            return
        for member in members:
            print(
                f"ID: {member.member_id} | Name: {member.name} | Email: {member.email} | Phone: {member.phone} | Status: {getattr(member, 'status', 'active')}"
            )

    @staticmethod
    def display_search_member_menu():
        print("\n===== Search Member =====")
        name = input("Name (partial or full): ")
        return name

    @staticmethod
    def display_member_history(history):
        print("\n===== Member Borrowing History =====")
        if not history:
            print("No borrowing history found.")
            return
        for borrowing in history:
            print(
                f"Book ID: {borrowing.book_id} | Borrowed: {borrowing.borrow_date} | Due: {borrowing.due_date} | Returned: {borrowing.return_date or 'Not returned'} | Status: {borrowing.status}"
            )

    @staticmethod
    def display_message(message):
        print(message)
