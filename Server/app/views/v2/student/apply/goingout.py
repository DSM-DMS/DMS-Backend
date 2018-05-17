from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.apply.goingout import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/apply/goingout'


@api.resource('')
class Goingout(BaseResource):
    @swag_from(GOINGOUT_GET)
    def get(self):
        pass

    @swag_from(GOINGOUT_POST)
    def post(self):
        pass