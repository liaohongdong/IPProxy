import sys
from werkzeug.wrappers import Response
from flask import Flask, jsonify, request

from Config.ConfigGetter import config

sys.path.append('../')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '123'


def run():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run()
