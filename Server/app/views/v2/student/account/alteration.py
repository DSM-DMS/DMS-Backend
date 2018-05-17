from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.alteration import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/account'


@api.resource('')
class Account(BaseResource):
    @swag_from(ACCOUNT_DELETE)
    def delete(self):
        pass


@api.resource('/change-pw')
class ChangePW(BaseResource):
    @swag_from(CHANGE_PW_POST)
    def post(self):
        pass
