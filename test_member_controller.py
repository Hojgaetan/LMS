import unittest
from controllers.member_controller import MemberController
from models.member import Member

class TestMemberController(unittest.TestCase):
    def setUp(self):
        # Clean up test members if needed
        for m in Member.find_by_name("Test User"):
            m.delete()
        for m in Member.find_by_name("Updated User"):
            m.delete()

    def test_add_member(self):
        success, msg = MemberController.add_member("Test User", email="testuser@example.com", phone="1234567890", address="Test Address")
        self.assertTrue(success)
        self.assertIn("added successfully", msg)
        # Clean up
        for m in Member.find_by_name("Test User"):
            m.delete()

    def test_update_member(self):
        # Add a member to update
        MemberController.add_member("Test User", email="testuser@example.com")
        member = Member.find_by_email("testuser@example.com")
        self.assertIsNotNone(member)
        success, msg = MemberController.update_member(member.member_id, name="Updated User")
        self.assertTrue(success)
        self.assertIn("updated successfully", msg)
        # Clean up
        for m in Member.find_by_name("Updated User"):
            m.delete()

    def test_delete_member(self):
        MemberController.add_member("Test User", email="testuser@example.com")
        member = Member.find_by_email("testuser@example.com")
        self.assertIsNotNone(member)
        success, msg = MemberController.delete_member(member.member_id)
        self.assertTrue(success)
        self.assertIn("deleted successfully", msg)

    def test_list_members(self):
        count_before = len(MemberController.list_members())
        MemberController.add_member("Test User", email="testuser@example.com")
        count_after = len(MemberController.list_members())
        self.assertGreaterEqual(count_after, count_before)
        # Clean up
        for m in Member.find_by_name("Test User"):
            m.delete()

    def test_search_members_by_name(self):
        MemberController.add_member("Test User", email="testuser@example.com")
        results = MemberController.search_members_by_name("Test User")
        self.assertTrue(any(m.name == "Test User" for m in results))
        # Clean up
        for m in Member.find_by_name("Test User"):
            m.delete()

    def test_set_member_status(self):
        MemberController.add_member("Test User", email="testuser@example.com")
        member = Member.find_by_email("testuser@example.com")
        self.assertIsNotNone(member)
        success, msg = MemberController.set_member_status(member.member_id, "inactive")
        self.assertTrue(success)
        self.assertIn("status updated", msg)
        member = Member.find_by_id(member.member_id)
        self.assertEqual(getattr(member, "status", "active"), "inactive")
        # Clean up
        member.delete()

if __name__ == "__main__":
    unittest.main()
