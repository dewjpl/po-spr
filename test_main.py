import unittest
import json
from main1 import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "age": 30,
            "group": "user"
        }
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data)
        self.assertEqual(user['firstName'], "John")
        self.assertEqual(user['lastName'], "Doe")
        self.assertEqual(user['age'], 30)
        self.assertEqual(user['group'], "user")

    def test_update_user(self):
        data = {
            "firstName": "Jane",
            "lastName": "Doe",
            "age": 15,
            "group": "premium"
        }
        response = self.app.patch('/users/1', json=data)
        self.assertEqual(response.status_code, 200)
        user = json.loads(response.data)
        self.assertEqual(user['firstName'], "Jane")
        self.assertEqual(user['age'], 15)
        self.assertEqual(user['group'], "premium")

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.data)
        self.assertIsInstance(users, list)



if __name__ == '__main__':
    unittest.main()
