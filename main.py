#!flask/bin/python
import os
from flask import Flask
from flask import request
from flask import jsonify

def split_data():
    # split train test and varification data here
    pass

def load_data():
    split_data()
    # load data here
    pass

def train_model():
    load_data()
    # train model here
    # store the model to filesystem
    pass

app = Flask(__name__)

@app.route('/isAlive', methods=['GET'])
def index():
    return jsonify(return_value = "channa")

if __name__ == '__main__':

    train_model()