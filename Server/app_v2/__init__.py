from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from app_v2.docs import TEMPLATE
from app_v2.models import Mongo
from app_v2.views import Router

from config_v2.dev import DevConfig
from config_v2.production import ProductionConfig


def create_app(dev=True):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    print('[INFO] Flask application initialized with {} mode.'.format('DEV' if dev else 'PRODUCTION'))

    app_ = Flask(__name__)
    app_.config.from_object(DevConfig if dev else ProductionConfig)

    JWTManager().init_app(app_)
    CORS().init_app(app_)
    Swagger(app_, template=TEMPLATE)
    Mongo().init_app(app_)
    Router().init_app(app_)

    return app_


app = create_app(False)


@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response
