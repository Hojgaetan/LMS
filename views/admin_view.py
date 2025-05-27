class AdminView:
    """View class for administrative operations."""

    @staticmethod
    def display_login_menu():
        print("\n===== Admin Login =====")
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    @staticmethod
    def display_config_menu():
        print("\n===== System Configuration =====")
        key = input("Config key: ")
        value = input("Config value: ")
        return key, value

    @staticmethod
    def display_backup_menu():
        print("\n===== Database Backup =====")
        path = input("Backup file path (leave empty for default): ")
        return path or None

    @staticmethod
    def display_restore_menu():
        print("\n===== Database Restore =====")
        path = input("Backup file path to restore: ")
        return path

    @staticmethod
    def display_message(message):
        print(message)
