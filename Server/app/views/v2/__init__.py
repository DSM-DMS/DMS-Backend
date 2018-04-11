from functools import wraps
import ujson
import time

from flask import Response, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app_v2.models import AdminModel, StudentModel, SystemModel


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response


def admin_only(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        g.user = admin
        return fn(*args, **kwargs)

    return wrapper


def student_only(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            abort(403)

        g.user = student
        return fn(*args, **kwargs)

    return wrapper


def system_only(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        system = SystemModel.objects(id=get_jwt_identity()).first()
        if not system:
            abort(403)

        g.user = system
        return fn(*args, **kwargs)

    return wrapper


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        student = StudentModel.objects(id=get_jwt_identity()).first()
        system = SystemModel.objects(id=get_jwt_identity()).first()

        if not any((admin, student, system)):
            abort(403)

        g.user = admin or student or system
        return fn(*args, **kwargs)

    return wrapper


def json_required(*required_keys):
    """
    View decorator for JSON validation.

    - If content-type is not application/json : returns status code 406
    - If required_keys are not exist on request.json : returns status code 400

    Args:
        *required_keys: Required keys on requested JSON payload
    """
    def decorator(fn):
        if fn.__name__ == 'get':
            print('[WARN] JSON with GET method? on "{}()"'.format(fn.__qualname__))

        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)

            for required_key in required_keys:
                if required_key not in request.json:
                    abort(400)

            return fn(*args, **kwargs)
        return wrapper

    return decorator


class BaseResource(Resource):
    """
    BaseResource with some helper functions based flask_restful.Resource
    """
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200, **kwargs):
        """
        Helper function which processes json response with unicode using ujson

        Args:
            data (dict or list): Data for dump to JSON
            status_code (int): Status code for response

        Returns:
            Response
        """
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8',
            **kwargs
        )


class Router(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.after_request(after_request)
