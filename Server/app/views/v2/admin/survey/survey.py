from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.survey.survey import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin'))


@api.resource('/survey')
class Survey(BaseResource):
    @swag_from(SURVEY_MANAGING_GET)
    def get(self):
        pass

    @swag_from(SURVEY_MANAGING_POST)
    def get(self):
        pass

    @swag_from(SURVEY_MANAGING_DELETE)
    def get(self):
        pass
