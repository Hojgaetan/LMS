from utils.db_utils import DatabaseConnection
import sqlite3
import os
from datetime import datetime


class AdminController:
    """Controller for administrative operations."""

    @staticmethod
    def authenticate_user(username, password):
        # Example: check in a 'users' table (not implemented here)
        # For demo, accept admin/admin
        if username == "admin" and password == "admin":
            return True, "Login successful."
        return False, "Invalid credentials."

    @staticmethod
    def set_config(key, value):
        # Example: store config in a table (not implemented here)
        # For demo, just print
        print(f"Config '{key}' set to '{value}' (not persisted in DB)")
        return True, f"Config '{key}' set to '{value}'."

    @staticmethod
    def backup_database(backup_path=None):
        src = "library.db"
        if not backup_path:
            backup_path = f"library_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        try:
            with open(src, "rb") as fsrc, open(backup_path, "wb") as fdst:
                fdst.write(fsrc.read())
            return True, f"Backup created at {backup_path}"
        except Exception as e:
            return False, str(e)

    @staticmethod
    def restore_database(backup_path):
        src = "library.db"
        try:
            with open(backup_path, "rb") as fsrc, open(src, "wb") as fdst:
                fdst.write(fsrc.read())
            return True, "Database restored from backup."
        except Exception as e:
            return False, str(e)

    @staticmethod
    def log_activity(action, user="system"):
        # Example: append to a log file
        with open("activity.log", "a") as log:
            log.write(f"{datetime.now()} | {user} | {action}\n")
