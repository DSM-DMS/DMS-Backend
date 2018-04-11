from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.docs import TEMPLATE
from app.models.v2 import Mongo
from app.views.v1 import Router

from config.v2.dev import DevConfig
from config.v2.production import ProductionConfig


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
