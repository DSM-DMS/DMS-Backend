import os
import threading
import time

from flask import current_app, jsonify, request, render_template
from werkzeug.exceptions import HTTPException

from app.views.v2 import BaseResource


def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    if not current_app.testing:
        current_app.config['INFLUXDB_CLIENT'].write_points([
            {
                'measurement': 'api_process_data',
                'tags': {
                    'status': response.status,
                    'method': request.method,
                    'uri': request.path
                },
                'fields': {
                    'count': 1
                }
            }
        ])

    return response


def exception_handler(e):
    print(e)

    if isinstance(e, HTTPException):
        description = e.description
        code = e.code
    else:
        description = ''
        code = 500

    return jsonify({
        'msg': description
    }), code


def index_student():
    return render_template('student.html')


def index_admin():
    return render_template('admin.html')


def reload_server():
    time.sleep(2)

    os.system('. ../hook.sh')


def webhook_event_handler():
    if request.headers['X-GitHub-Event'] == 'push':
        threading.Thread(target=reload_server).start()

    return 'hello'
