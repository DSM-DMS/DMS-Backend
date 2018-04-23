from functools import wraps
import ujson
import time

from flask import Response, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.models.account import AdminModel, StudentModel, SystemModel

MODEL_DOCSTRING_MAPPING = {
    AdminModel: ' *관리자 권한',
    StudentModel: ' *학생 권한',
    SystemModel: ' *시스템 권한'
}


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response


def auth_required(model):
    def decorator(fn):
        fn.__doc__ = fn.__doc__[:-9] + MODEL_DOCSTRING_MAPPING[model] + fn.__doc__[-9:]

        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            user = model.objects(id=get_jwt_identity()).first()
            if not user:
                abort(403)

            g.user = user
            return fn(*args, **kwargs)

        return wrapper
    return decorator


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

        from .admin.account import account_management, auth
        app.register_blueprint(account_management.api.blueprint)
        app.register_blueprint(auth.api.blueprint)

        from .admin.excel import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from .admin.point import point, rule, student
        app.register_blueprint(point.api.blueprint)
        app.register_blueprint(rule.api.blueprint)
        app.register_blueprint(student.api.blueprint)

        from .admin.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from .admin.report import facility
        app.register_blueprint(facility.api.blueprint)

        from .admin.survey import question, survey
        app.register_blueprint(question.api.blueprint)
        app.register_blueprint(survey.api.blueprint)

        from .mixed.jwt import checker, refresh
        app.register_blueprint(checker.api.blueprint)
        app.register_blueprint(refresh.api.blueprint)

        from .mixed.metadata import developers, links
        app.register_blueprint(developers.api.blueprint)
        app.register_blueprint(links.api.blueprint)

        from .mixed.post import post, preview
        app.register_blueprint(post.api.blueprint)
        app.register_blueprint(preview.api.blueprint)

        from .mixed.school_data import meal
        app.register_blueprint(meal.api.blueprint)

        from .student.account import alteration, auth, info, signup, social_auth
        app.register_blueprint(alteration.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(info.api.blueprint)
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(social_auth.api.blueprint)

        from .student.apply import extension
        app.register_blueprint(extension.api.blueprint)
