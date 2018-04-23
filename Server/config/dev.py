from config import Config


class DevConfig(Config):
    HOST = 'localhost'
    PORT = 8000

    Config.SWAGGER['host'] = '{}:{}'.format(Config.REPRESENTATIVE_HOST or HOST, PORT)

    DEBUG = True

    MONGODB_SETTINGS = {
        'host': 'localhost',
        'port': 27017,
        'db': '{}-dev'.format(Config.SERVICE_NAME)
    }
