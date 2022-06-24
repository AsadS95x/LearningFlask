from application import app
from flask import render_template
import requests

@app.route('/', methods=['GET'])
def get_text():
        chars = requests.get('http://Service2:5000/get_text').text
        nums = requests.get('http://Service3:5000/get_nums').text
        prize = requests.post('http://Service4:5000/prize', json=dict(chars=chars, nums=nums))
        return render_template('home.html', chars=chars, nums=nums, prize=prize.text)

        