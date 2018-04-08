from functools import wraps
import ujson
import time

from flask import Response, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app_v1.models.account import AdminModel, StudentModel, SystemModel


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


class BaseResource(Resource):
    """
    BaseResource with some helper functions based flask_restful.Resource
    """
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_response(cls, data, status_code=200):
        """
        Helper function which processes json response with unicode using ujson

        - About ujson.dumps(data, ensure_ascii=False)
        If ensure_ascii is true (the default),
        all non-ASCII characters in the output are escaped with \\uXXXX sequences,
        and the result is a str instance consisting of ASCII characters only.
        If ensure_ascii is false, some chunks written to fp may be unicode instances.

        :type data: dict or list
        :type status_code: int

        :rtype: Response
        """
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )


class Router(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app_v1.views.admin.account import account_control, auth, signup
        app.register_blueprint(account_control.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app_v1.views.admin.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app_v1.views.admin.point import point, rule, student
        app.register_blueprint(point.api.blueprint)
        app.register_blueprint(rule.api.blueprint)
        app.register_blueprint(student.api.blueprint)

        from app_v1.views.admin.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app_v1.views.admin.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app_v1.views.admin.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app_v1.views.student.account import alteration, auth, info, signup
        app.register_blueprint(alteration.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(info.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app_v1.views.student.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app_v1.views.student.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app_v1.views.student.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app_v1.views.mixed.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app_v1.views.mixed.school_data import meal
        app.register_blueprint(meal.api.blueprint)

        from app_v1.views.system import account_management, apply_management, auth
        app.register_blueprint(account_management.api.blueprint)
        app.register_blueprint(apply_management.api.blueprint)
        app.register_blueprint(auth.api.blueprint)

        from app_v1.views import app_version_checker
        app.register_blueprint(app_version_checker.api.blueprint)
