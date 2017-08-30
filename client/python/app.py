from flask import Flask, request, abort
import random
app = Flask(__name__)

import json
import time

@app.route('/', methods=['GET'])
def hello():
    return 'salam!'

@app.route('/placing', methods=['POST'])
def placing():
    data = request.data
    dataDict = json.loads(data)
    print dataDict
    return json.dumps({
        'selectedPosition': random.randint(0, 23)
    })