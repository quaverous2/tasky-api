import unittest
from app import create_app, db

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_task(self):
        response = self.client.post('/tasks', json={
            "title": "Test Task",
            "description": "This is a test task."
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()