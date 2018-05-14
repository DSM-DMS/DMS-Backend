from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.apply.stay import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/apply/stay'


@api.resource('/')
class Stay(BaseResource):
    @swag_from(STAY_GET)
    def get(self):
        pass

    @swag_from(STAY_POST)
    def post(self):
        pass
