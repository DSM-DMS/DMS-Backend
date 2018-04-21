from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.rule import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/point/rule', __name__, url_prefix='/admin/point'))


@api.resource('/rule')
class Rule(BaseResource):
    @swag_from(POINT_RULE_GET)
    def get(self):
        pass

    @swag_from(POINT_RULE_POST)
    def get(self):
        pass

    @swag_from(POINT_RULE_PATCH)
    def patch(self):
        pass

    @swag_from(POINT_RULE_DELETE)
    def delete(self):
        pass
