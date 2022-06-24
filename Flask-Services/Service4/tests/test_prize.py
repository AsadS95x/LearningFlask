from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes

class TestBase(TestCase):
        def create_app(self):
            return app
        
class TestPrize(TestBase):
    @patch('application.routes.choice', return_value='50')
    def test_prize(self, patched):
            response = self.client.post(url_for('prize'), json ={'chars':'abc', 'nums':'123456'})
            self.assert200(response)
            self.assertIn(b'50', response.data)


    

