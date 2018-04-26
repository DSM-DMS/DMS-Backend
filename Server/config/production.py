import socket

from config import Config


class ProductionConfig(Config):
    HOST = socket.gethostbyname(socket.gethostname())

    Config.SWAGGER['host'] = '{}:{}'.format(Config.REPRESENTATIVE_HOST or HOST, Config.PORT)

    DEBUG = False

    Config.MONGODB_SETTINGS.update({
        'db': Config.SERVICE_NAME
    })
