import os

from flask import current_app, request, render_template
from werkzeug.exceptions import HTTPException


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    current_app.config['INFLUX_DB_CLIENT'].write_points([
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
    current_app.config['INFLUX_DB_CLIENT'].write_points([
        {
            'measurement': 'api_process_data',
            'tags': {
                'status': 500,
                'method': request.method,
                'uri': request.path
            },
            'fields': {
                'count': 1
            }
        }
    ])

    print(e)

    if isinstance(e, HTTPException):
        return e.description, e.code
    else:
        return '', 500


def index_student():
    return render_template('student.html')


def index_admin():
    return render_template('admin.html')


def webhook_event_handler():
    if request.headers['X-GitHub-Event'] == 'push':
        os.system('. ../hook.sh')

    return 'hello'
