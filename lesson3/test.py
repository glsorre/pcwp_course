import base64
import unittest
from lesson3.exercise import app as web_app

class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        web_app.testing = True
        self.app = web_app.test_client()

    def test_unrestricted(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertDictEqual(result.get_json() , {
            "200": "Unrestricted Access"
        })

    def test_restricted_noauth(self):
        result = self.app.get('/restricted')
        self.assertEqual(result.status_code, 401)
        self.assertDictEqual(result.get_json() , {
            "401": "Unauthorized"
        })

    def test_restricted_withauth(self):
        valid_credentials = base64.b64encode(b'gsorrentino:password').decode('utf-8')
        result = self.app.get('/restricted', headers={'Authorization': 'Basic ' + valid_credentials})
        self.assertEqual(result.status_code, 200)
        self.assertDictEqual(result.get_json() , {
            "200": "Authorized"
        })

if __name__ == '__main__':
    unittest.main()