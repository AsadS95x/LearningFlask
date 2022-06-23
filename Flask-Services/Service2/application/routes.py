from application import app
from random import choice

@app.route('/get_text', methods=['GET'])
def get_text():
        alphabert = 'abcdefghijklmnopqrstuvxwyz'
        text = ''.join(choice(alphabert) for _ in range(3))
        return text

        