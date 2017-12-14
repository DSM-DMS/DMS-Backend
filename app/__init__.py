from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from app.docs import TEMPLATE
from app.models import Mongo
from app.views import ViewInjector
from app.middleware import ErrorHandler, Logger

cors = CORS()
jwt = JWTManager()
swagger = Swagger(template=TEMPLATE)
error_handler = ErrorHandler()
logger = Logger()
db = Mongo()
view = ViewInjector()


def create_app(config_name):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    app_ = Flask(__name__)
    app_.config.from_pyfile(config_name)

    cors.init_app(app_)
    jwt.init_app(app_)
    swagger.init_app(app_)
    error_handler.init_app(app_)
    logger.init_app(app_)
    db.init_app(app_)
    view.init_app(app_)

    return app_

app = create_app('../config/dev.py')
