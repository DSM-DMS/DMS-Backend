from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.rule import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/post/rule', __name__, url_prefix='/admin'))


@api.resource('/rule')
class Rule(BaseResource):
    @swag_from(RULE_POST)
    def post(self):
        pass

    @swag_from(RULE_PATCH)
    def patch(self):
        pass

    @swag_from(RULE_DELETE)
    def delete(self):
        pass
