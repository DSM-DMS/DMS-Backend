from functools import wraps

import json
import time

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, abort

from app.models.account import AdminModel, StudentModel


class AccessControl(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.errorhandler(_Forbidden)
        def forbidden_handler(e):
            return abort(403)


class _Forbidden(Exception):
    pass


class BaseResource(Resource):
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_response(cls, data, status_code=200):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

    @classmethod
    def admin_only(cls, fn):
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
                raise _Forbidden

            return fn(*args, **kwargs)

        return wrapper

    @classmethod
    def student_only(cls, fn):
        fn = jwt_required(fn)

        @wraps(fn)
        def wrapper(*args, **kwargs):
            fn(*args, **kwargs)

            student = StudentModel.objects(id=get_jwt_identity())
            if not student:
                raise _Forbidden

            return fn(*args, **kwargs)

        return wrapper

    @classmethod
    def signed_account_only(cls, fn):
        fn = jwt_required(fn)

        @wraps(fn)
        def wrapper(*args, **kwargs):
            fn(*args, **kwargs)

            admin = AdminModel.objects(id=get_jwt_identity())
            student = StudentModel.objects(id=get_jwt_identity())

            if not any((admin, student)):
                raise _Forbidden

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
