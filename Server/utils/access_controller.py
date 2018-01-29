from functools import wraps

from flask import abort
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.account import AdminModel, StudentModel


class Forbidden(Exception):
    pass


class AccessControl(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.errorhandler(Forbidden)
        def forbidden_handler(e):
            return abort(403)


def admin_only(fn):
    fn = jwt_required(fn)
    # wrapper 반환받음

    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        # wrapper 안에서 실제로 request를 뜯어 JWT token을 가져옴.
        # 1. get_jwt_identity() 시 제대로된 값을 반환받기 위해서
        # 2. Application context 관련 문제가 없도록

        admin = AdminModel.objects(id=get_jwt_identity())
        if not admin:
            raise Forbidden

        return fn(*args, **kwargs)
    return wrapper


def student_only(fn):
    fn = jwt_required(fn)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

        student = StudentModel.objects(id=get_jwt_identity())
        if not student:
            raise Forbidden

        return fn(*args, **kwargs)
    return wrapper


def signed_account_only(fn):
    fn = jwt_required(fn)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

        admin = AdminModel.objects(id=get_jwt_identity())
        student = StudentModel.objects(id=get_jwt_identity())

        if not any((admin, student)):
            raise Forbidden

        return fn(*args, **kwargs)
    return wrapper
