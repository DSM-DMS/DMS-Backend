import socket
import os

import json
from flask import Flask, request

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def event_handler():
        payload = request.json

        if request.headers['X-GitHub-Event'] == 'push':
            print('push!')
            os.system('. hook.sh')

        return 'hello'


    app.run(host=HOST, port=PORT, threaded=True)
