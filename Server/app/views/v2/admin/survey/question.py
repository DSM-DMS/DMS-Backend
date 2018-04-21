from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.survey.question import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/survey/question', __name__, url_prefix='/admin/survey'))


@api.resource('/question')
class Question(BaseResource):
    @swag_from(QUESTION_MANAGING_GET)
    def get(self):
        pass

    @swag_from(QUESTION_MANAGING_POST)
    def post(self):
        pass
