from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.post import *
from app.models.account import AdminModel
from app.models.post import FAQModel, NoticeModel, RuleModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/post'))


@api.resource('/<category>')
class Post(BaseResource):
    @swag_from(POST_POST)
    def post(self, category):
        pass


@api.resource('/<category>/<post_id>')
class PostAlteration(BaseResource):
    @swag_from(POST_PATCH)
    def patch(self, post_id):
        pass

    @swag_from(POST_DELETE)
    def delete(self, post_id):
        pass
