from functools import wraps
from uuid import UUID
import ujson
import time

from flask import Response, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.models.account import AdminModel, StudentModel
from app.models.token import AccessTokenModelV2


def admin_only(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        token = AccessTokenModelV2.objects(identity=UUID(get_jwt_identity())).first()

        if token and isinstance(token.key.owner, AdminModel):
            g.user = token.key.owner
        else:
            abort(403)

        return fn(*args, **kwargs)
    return wrapper


def student_only(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        token = AccessTokenModelV2.objects(identity=UUID(get_jwt_identity())).first()

        if token and isinstance(token.key.owner, StudentModel):
            g.user = token.key.owner
        else:
            abort(403)

        return fn(*args, **kwargs)
    return wrapper


def auth_required(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        token = AccessTokenModelV2.objects(identity=UUID(get_jwt_identity())).first()

        if token:
            g.user = token.owner
        else:
            abort(403)

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


class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.views.v1.admin.account import account_control, auth, signup
        app.register_blueprint(account_control.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app.views.v1.admin.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app.views.v1.admin.point import point, rule, student
        app.register_blueprint(point.api.blueprint)
        app.register_blueprint(rule.api.blueprint)
        app.register_blueprint(student.api.blueprint)

        from app.views.v1.admin.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app.views.v1.admin.report import facility_report
        app.register_blueprint(facility_report.api.blueprint)

        from app.views.v1.admin.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app.views.v1.student.account import alteration, auth, info, signup
        app.register_blueprint(alteration.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(info.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app.views.v1.student.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app.views.v1.student.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app.views.v1.student.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app.views.v1.mixed.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app.views.v1.mixed.school_data import meal
        app.register_blueprint(meal.api.blueprint)

        from app.views.v1 import app_version_checker
        app.register_blueprint(app_version_checker.api.blueprint)
