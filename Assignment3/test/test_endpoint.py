import unittest
import base64
from src.main import app


class SignupTest(unittest.TestCase):
  def test_login(self):
      with app.app_context():
          tester = app.test_client(self)
         
          response = tester.get("/login",headers={"Authorization": "Basic {}".format(base64.b64encode(b"admin:password").decode("utf8"))})
          self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()