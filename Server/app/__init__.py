from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from mongoengine import connect
# from redis import Redis
from influxdb import InfluxDBClient

from app.views.v1 import Router as V1Router
from app.views.v2 import Router as V2Router
from app.views import *

WEB_FILE_ROOT_DIR = '../web_files'


def create_app(*config_cls):
    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    app_ = Flask(
        __name__,
        static_folder='{}/static'.format(WEB_FILE_ROOT_DIR),
        template_folder='{}/templates'.format(WEB_FILE_ROOT_DIR)
    )

    for config in config_cls:
        app_.config.from_object(config)

    connect(**app_.config['MONGODB_SETTINGS'])
    # app_.config['REDIS_CLIENT'] = Redis(**app_.config['REDIS_SETTINGS'])

    if not app_.testing:
        app_.config['INFLUXDB_CLIENT'] = InfluxDBClient(**app_.config['INFLUXDB_SETTINGS'])

        cfg = app_.config

        if cfg['INFLUXDB_SETTINGS']['database'] not in cfg['INFLUXDB_CLIENT'].get_list_database():
            cfg['INFLUXDB_CLIENT'].create_database(cfg['INFLUXDB_SETTINGS']['database'])

    JWTManager().init_app(app_)
    CORS().init_app(app_)
    Swagger(template=app_.config['SWAGGER_TEMPLATE']).init_app(app_)

    V1Router().init_app(app_)
    V2Router().init_app(app_)

    app_.after_request(after_request)
    app_.register_error_handler(Exception, exception_handler)
    app_.add_url_rule('/', view_func=index_student)
    app_.add_url_rule('/admin', view_func=index_admin)
    app_.add_url_rule('/hook', view_func=webhook_event_handler, methods=['POST'])

    return app_
