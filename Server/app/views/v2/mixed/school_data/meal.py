from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.school_data.meal import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/meal'


@api.resource('')
class Meal(BaseResource):
    @swag_from(MEAL_GET)
    def get(self):
        pass