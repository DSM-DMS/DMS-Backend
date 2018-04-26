from flask import request, render_template


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    from utils.influxdb import c as influx_client

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    influx_client.write_points([
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


def index_student():
    return render_template('student.html')


def index_admin():
    return render_template('admin.html')
