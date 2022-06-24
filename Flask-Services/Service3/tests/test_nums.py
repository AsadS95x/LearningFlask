from application import app
import applcation.routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
        def create_app(self):
            return app
        
class TestChars(TestBase):
    @patch('application.routes.crandinthoice', return_value='123456')
    def test_get_num_a(self, patched):
        response = self.client.get(url_for('get_nums'))
        self.assert200(response)
        self.assertIn(b'123456', response.data)

class TestChars(TestBase):
    @patch('application.routes.choice', return_value='987654')
    def test_get_num_b(self, patched):
        response = self.client.get(url_for('get_text'))
        self.assert200(response)
        self.assertIn(b'987654', response.data)

