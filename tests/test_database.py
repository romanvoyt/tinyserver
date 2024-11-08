import unittest
from db.database import init_db, create_user, get_all_users

class TestDatabase(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_create_user(self):
        user_id = create_user("Test User", 30)
        self.assertIsNotNone(user_id)

    def test_get_all_users(self):
        users = get_all_users()
        self.assertIsInstance(users, list)

if __name__ == "__main__":
    unittest.main()
