from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.auth import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/account/auth', __name__, url_prefix='/admin'))


@api.resource('/auth')
class Auth(BaseResource):
    @swag_from(AUTH_POST)
    def post(self):
        pass
