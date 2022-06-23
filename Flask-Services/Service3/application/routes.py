from application import app
from random import randint

@app.route('/get_nums', methods=['GEt'])
def get_nums():
        nums = randint(10000, 999999)
        return str(nums)