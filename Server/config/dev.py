from config import Config


class DevConfig(Config):
    HOST = 'localhost'
    ENDPOINT = '{}:{}'.format(HOST, Config.PORT)
    Config.SWAGGER.update({'host': ENDPOINT})

    TEST = True
    DEBUG = True

    MONGODB_SETTINGS = {
        'host': 'localhost',
        'port': 27017,
        'db': '{}-dev'.format(Config.SERVICE_NAME)
    }
