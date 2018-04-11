from mongoengine import *


class Mongo(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        setting = app.config['MONGODB_SETTINGS']

        connect(setting['db'], host=setting['host'], port=setting['port'])
