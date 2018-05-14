from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.signup import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student'


@api.resource('/verify/id')
class IDVerification(BaseResource):
    @swag_from(ID_VERIFICATION_POST)
    def post(self):
        pass


@api.resource('/verify/uuid')
class UUIDVerification(BaseResource):
    @swag_from(UUID_VERIFICATION_POST)
    def post(self):
        pass


@api.resource('/signup')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        pass
