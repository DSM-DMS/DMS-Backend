from functools import wraps

import ujson
import time

from flask import Response, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.account import AdminModel, StudentModel, SystemModel


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

    @staticmethod
    def admin_only(fn):
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            admin = AdminModel.objects(id=get_jwt_identity()).first()
            if not admin:
                abort(403)

            return fn(*args, **kwargs)

        return wrapper

    @staticmethod
    def student_only(fn):
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            student = StudentModel.objects(id=get_jwt_identity()).first()
            if not student:
                abort(403)

            return fn(*args, **kwargs)

        return wrapper

    @staticmethod
    def system_only(fn):
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            system = SystemModel.objects(id=get_jwt_identity()).first()
            if not system:
                abort(403)

            return fn(*args, **kwargs)

        return wrapper

    @staticmethod
    def signed_account_only(fn):
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            admin = AdminModel.objects(id=get_jwt_identity()).first()
            student = StudentModel.objects(id=get_jwt_identity()).first()

            if not any((admin, student)):
                abort(403)

            return fn(*args, **kwargs)

        return wrapper


class Router(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.views.admin.account import account_control, auth, signup
        app.register_blueprint(account_control.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app.views.admin.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app.views.admin.point import point, rule, student
        app.register_blueprint(point.api.blueprint)
        app.register_blueprint(rule.api.blueprint)
        app.register_blueprint(student.api.blueprint)

        from app.views.admin.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app.views.admin.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app.views.admin.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app.views.student.account import alteration, auth, info, signup
        app.register_blueprint(alteration.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(info.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app.views.student.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app.views.student.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app.views.student.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app.views.mixed.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app.views.mixed.school_data import meal
        app.register_blueprint(meal.api.blueprint)

        from app.views.system import account_management, apply_management, auth
        app.register_blueprint(account_management.api.blueprint)
        app.register_blueprint(apply_management.api.blueprint)
        app.register_blueprint(auth.api.blueprint)

        from app.views import app_version_checker
        app.register_blueprint(app_version_checker.api.blueprint)
