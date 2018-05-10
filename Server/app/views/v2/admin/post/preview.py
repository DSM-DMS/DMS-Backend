from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.preview import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/post/preview'))


@api.resource('/faq')
class FAQ(BaseResource):
    @swag_from(FAQ_PREVIEW_POST)
    def post(self):
        pass


@api.resource('/notice')
class Notice(BaseResource):
    @swag_from(NOTICE_PREVIEW_POST)
    def post(self):
        pass


@api.resource('/rule')
class Rule(BaseResource):
    @swag_from(RULE_PREVIEW_POST)
    def post(self):
        pass
