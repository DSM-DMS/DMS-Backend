from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.faq import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/post'))


@api.resource('/faq')
class FAQ(BaseResource):
    @swag_from(FAQ_POST)
    def post(self):
        pass


@api.resource('/faq/<post_id>')
class FAQAlteration(BaseResource):
    @swag_from(FAQ_PATCH)
    def patch(self, post_id):
        pass

    @swag_from(FAQ_DELETE)
    def delete(self, post_id):
        pass
