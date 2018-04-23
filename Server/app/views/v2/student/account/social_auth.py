from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.social_auth import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/student/social-account'))


@api.resource('/add')
class AddSocialAccount(BaseResource):
    @swag_from(ADD_SOCIAL_ACCOUNT_POST)
    def post(self):
        pass


@api.resource('/auth')
class SocialAuth(BaseResource):
    @swag_from(SOCIAL_AUTH_POST)
    def post(self):
        pass
