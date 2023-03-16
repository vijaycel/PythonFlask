import json
from flask import Flask, jsonify
from urllib.request import urlopen 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/user', methods=['GET'])
def user():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})


@app.route('/shipmentcost', methods=['GET'])
def shipmentcost():
    with urlopen('http://127.0.0.1:3000/reports/filecheck') as r:
        text = r.read()
    return text


