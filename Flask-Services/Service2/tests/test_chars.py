from application import app
import application.routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
        def create_app(self):
            return app
        
class TestChars(TestBase):
    @patch('application.routes.choice', return_value='a')
    def test_get_chars_a(self, patched):
        response = self.client.get(url_for('get_text'))
        self.assert200(response)
        self.assertIn(b'aaa', response.data)

class TestChars2(TestBase):
    @patch('application.routes.choice', return_value='b')
    def test_get_chars_b(self, patched):
        response = self.client.get(url_for('get_text'))
        self.assert200(response)
        self.assertIn(b'bbb', response.data)

