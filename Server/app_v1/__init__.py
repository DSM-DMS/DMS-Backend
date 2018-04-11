from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from app_v1.docs import TEMPLATE
from app_v2.models import Mongo
from app_v1.views import Router

from config_v1.dev import DevConfig
from config_v1.production import ProductionConfig


def create_app(dev=True):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    app_ = Flask(__name__)
    app_.config.from_object(DevConfig if dev else ProductionConfig)

    JWTManager().init_app(app_)
    CORS().init_app(app_)
    # Swagger(app_, template=TEMPLATE)
    Mongo().init_app(app_)
    Router().init_app(app_)

    return app_


app = create_app(False)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response
