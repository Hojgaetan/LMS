import unittest
import os
from controllers.admin_controller import AdminController

class TestAdminController(unittest.TestCase):
    def test_authenticate_user(self):
        success, msg = AdminController.authenticate_user("admin", "admin")
        self.assertTrue(success)
        self.assertIn("Login successful", msg)
        fail, msg = AdminController.authenticate_user("user", "wrong")
        self.assertFalse(fail)
        self.assertIn("Invalid credentials", msg)

    def test_set_config(self):
        success, msg = AdminController.set_config("max_borrow_days", 21)
        self.assertTrue(success)
        self.assertIn("max_borrow_days", msg)

    def test_backup_and_restore_database(self):
        backup_path = "test_backup.db"
        # Backup
        success, msg = AdminController.backup_database(backup_path)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(backup_path))
        # Restore
        success, msg = AdminController.restore_database(backup_path)
        self.assertTrue(success)
        # Cleanup
        if os.path.exists(backup_path):
            os.remove(backup_path)

    def test_log_activity(self):
        log_file = "activity.log"
        if os.path.exists(log_file):
            os.remove(log_file)
        AdminController.log_activity("Test action", user="testuser")
        self.assertTrue(os.path.exists(log_file))
        with open(log_file, "r") as f:
            content = f.read()
            self.assertIn("Test action", content)
            self.assertIn("testuser", content)
        os.remove(log_file)

if __name__ == "__main__":
    unittest.main()
