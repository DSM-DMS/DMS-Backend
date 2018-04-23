from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.jwt.checker import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/jwt'))


@api.resource('/check')
class AuthCheck(BaseResource):
    @swag_from(AUTH_CHECK_GET)
    def get(self):
        pass
