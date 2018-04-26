from datetime import timedelta
import os


class Config(object):
    REPRESENTATIVE_HOST = 'dsm2015.cafe24.com'
    PORT = 80
    SERVICE_NAME = 'dms-v2'

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')
    # Secret key for any 3-rd party libraries

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    JWT_HEADER_TYPE = 'JWT'

    MONGODB_SETTINGS = {
        'host': 'localhost',
        'port': 27017,
        'username': os.getenv('MONGO_ID'),
        'password': os.getenv('MONGO_PW')
    }

    INFLUX_DB_SETTINGS = {
        'db': SERVICE_NAME.replace('-', '_')
    }

    SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/'
    }


    }
