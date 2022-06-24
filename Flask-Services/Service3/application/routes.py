from application import app
from random import randint

@app.route('/get_nums', methods=['GET'])
def get_nums():
        nums = randint(100000, 999999)
        print(nums)
        print(nums)
        print(nums)
        print(nums)
        print(nums)
        print(nums)
        print(nums)
        print(nums)
        return str(nums)