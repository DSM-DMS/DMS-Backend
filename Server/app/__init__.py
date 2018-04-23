from flask import Blueprint, Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from app.models import Mongo
from app.views.v1 import Router

from config.dev import DevConfig
from config.production import ProductionConfig

WEB_FILE_ROOT_DIR = '../web_files'


def create_app(dev=True):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    print('[INFO] Flask application initialized with {} mode.'.format('DEV' if dev else 'PRODUCTION'))

    app_ = Flask(
        __name__,
        static_folder='{}/static'.format(WEB_FILE_ROOT_DIR),
        template_folder='{}/templates'.format(WEB_FILE_ROOT_DIR)
    )

    app_.config.from_object(DevConfig if dev else ProductionConfig)

    JWTManager().init_app(app_)
    CORS().init_app(app_)
    Mongo().init_app(app_)
    Router().init_app(app_)

    return app_


def merge_v2_api(app_):
    from app.views.v2 import Router
    from app.docs.v2 import TEMPLATE

    app_.config['SWAGGER']['specs_route'] = '/v2/docs'
    app_.config['basePath'] = '/v2'

    Swagger(template=TEMPLATE).init_app(app_)
    Router().init_app(app_)


app = create_app(False)
merge_v2_api(app)


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
