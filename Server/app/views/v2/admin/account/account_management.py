from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.account_management import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/account-management'))


@api.resource('/student')
class StudentAccount(BaseResource):
    @swag_from(STUDENT_ACCOUNT_DELETE)
    def delete(self):
        pass


@api.resource('/admin')
class AdminAccount(BaseResource):
    @swag_from(ADMIN_ACCOUNT_DELETE)
    def delete(self):
        pass
