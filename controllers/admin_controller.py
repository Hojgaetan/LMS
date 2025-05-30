from services.admin_service import AdminService


class AdminController:
    """Controller for administrative operations."""

    @staticmethod
    def authenticate_user(username, password):
        return AdminService.authenticate_user(username, password)

    @staticmethod
    def set_config(key, value):
        return AdminService.set_config(key, value)

    @staticmethod
    def backup_database(backup_path=None):
        return AdminService.backup_database(backup_path)

    @staticmethod
    def restore_database(backup_path):
        return AdminService.restore_database(backup_path)

    @staticmethod
    def log_activity(action, user="system"):
        return AdminService.log_activity(action, user)
