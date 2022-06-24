from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
        def create_app(self):
            return app
        
class TestFront(TestBase):
    def test_get_front(self):
        with requests_mock.Mocker() as m:
            m.get('http://Service2:5000/get_text', text = 'abc')
            m.get('http://Service3:5000/get_nums', text = '123456')
            m.post('http://Service4:5000/prize', text = '£50')
            response = self.client.get(url_for('get_text'))
            self.assert200(response)
            self.assertIn(b'50', response.data)

class TestFront2(TestBase):
    def test_get_front_again(self):
        with requests_mock.Mocker() as m:
            m.get('http://Service2:5000/get_text', text = 'def')
            m.get('http://Service3:5000/get_nums', text = '456789')
            m.post('http://Service4:5000/prize', text = 'No prize for you')
            response = self.client.get(url_for('get_text'))
            self.assert200(response)
            self.assertIn(b'You won: No prize for you', response.data)


    

