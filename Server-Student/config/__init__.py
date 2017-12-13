import os
from datetime import timedelta

PORT = 3000

SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')
# Secret key for any 3-rd party libraries

JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=3)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1000)
JWT_HEADER_TYPE = 'JWT'
# http://flask-jwt-extended.readthedocs.io/en/latest/options.html

SERVICE_NAME = 'DMS'

SWAGGER = {
    'title': SERVICE_NAME,
    'specs_route': '/docs/',
    'uiversion': 3,

    'info': {
        'title': SERVICE_NAME + ' API',
        'version': '1.0',
        'description': '''
JWT Access Token의 유효기간은 {0}일, Refresh Token의 유효기간은 {1}일입니다.

- Status Code 1xx : Informational
- Status Code 2xx : Success
- Status Code 3xx : Redirection
- Status Code 4xx : Client Error
- Status Code 5xx : Server Error

##### <a href="https://httpstatuses.com/">[All of HTTP status code]</a>
##### <a href="http://meetup.toast.com/posts/92">[About REST API]</a>
##### <a href="http://jinja.pocoo.org/docs/2.10/">[About Jinja2]</a>
##### <a href="https://velopert.com/2389">[About JWT]</a>
'''.format(JWT_ACCESS_TOKEN_EXPIRES.days, JWT_REFRESH_TOKEN_EXPIRES.days)
    },

    'basePath': '/ '
}
