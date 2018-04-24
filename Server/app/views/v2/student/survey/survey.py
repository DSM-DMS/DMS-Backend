from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.survey.survey import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/student/survey'))


@api.resource('/list')
class Survey(BaseResource):
    @swag_from(SURVEY_GET)
    def get(self):
        pass


@api.resource('/question')
class Question(BaseResource):
    @swag_from(QUESTION_GET)
    def get(self):
        pass

    @swag_from(QUESTION_POST)
    def post(self):
        pass
