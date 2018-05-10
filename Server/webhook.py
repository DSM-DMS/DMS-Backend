import socket

import json
from flask import Flask, request

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/postreceive', methods=['POST'])
    def event_handler():
        payload = request.json
        print(json.dumps(payload, indent=4))
        print('Working!')

        return 'hello'


    app.run(host=HOST, port=PORT, threaded=True)
