from flask import request, render_template


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    from utils.influxdb import c as influx_client

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    # influx_client.write_points([
    #     {
    #         'measurement': 'req_res_data',
    #         'tags': {
    #             'status': response.status,
    #             'uri': request.path
    #         },
    #         'fields': {
    #             'value': 1
    #         }
    #     }
    # ])

    influx_client.write_points([
        {
            'measurement': 'response_status',
            'tags': {
                'status': response.status
            },
            'fields': {
                'value': 1
            }
        }
    ])

    influx_client.write_points([
        {
            'measurement': 'request_data',
            'tags': {
                'uri': request.path
            },
            'fields': {
                'value': 1
            }
        }
    ])

    return response


def index_student():
    return render_template('student.html')


def index_admin():
    return render_template('admin.html')
