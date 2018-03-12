from functools import wraps

from flask import g, request
from flask_restful import abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.account import AdminModel, StudentModel, SystemModel


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

    :type required_keys: str
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
