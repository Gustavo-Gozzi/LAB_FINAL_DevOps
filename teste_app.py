import unittest
from app import app
import werkzeug

werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"
class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def test_home(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items":["XBOX","PlayStation","Nintendo Switch"]})

    def test_login(self):
#a
        response = self.client.get('/login')
        self.assertNotEqual(response.status_code, 200)
    
    def test_protected_with_token(self):
        response = self.client.post('/login')
        token = response.json['acess_token']
        headers = {
            'Authorization': f'Bearer {token}' 
        }
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)

#oi

if __name__ == '__main__':
    unittest.main()