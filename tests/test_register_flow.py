import unittest
import json
from app import app, db
from models.user_model import User

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_success(self):
        response = self.client.post('/api/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User registered successfully')

    def test_register_duplicate_username(self):
        # First registration
        self.client.post('/api/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        })
        # Duplicate registration
        response = self.client.post('/api/register', json={
            'username': 'testuser',
            'email': 'other@example.com',
            'password': 'password456'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Username already exists')

    def test_register_missing_fields(self):
        response = self.client.post('/api/register', json={
            'username': 'testuser'
            # Missing email and password
        })
        self.assertEqual(response.status_code, 400)
