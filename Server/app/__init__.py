from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from app.docs import TEMPLATE
from app.models import Mongo
from app.views import ViewInjector

from config.dev import DevConfig
from config.production import ProductionConfig

jwt = JWTManager()
cors = CORS()
swagger = Swagger(template=TEMPLATE)

db = Mongo()
view = ViewInjector()


def create_app(dev=True):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    app_ = Flask(__name__)
    app_.config.from_object(DevConfig if dev else ProductionConfig)

    jwt.init_app(app_)
    cors.init_app(app_)
    swagger.init_app(app_)
    db.init_app(app_)
    view.init_app(app_)

    return app_


app = create_app()


@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'
    response.headers['Content-Security-Policy'] = 'default-src \'none\''

    return response
