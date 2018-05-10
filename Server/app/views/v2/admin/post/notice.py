from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.notice import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/post'))


@api.resource('/notice')
class Notice(BaseResource):
    @swag_from(NOTICE_POST)
    def post(self):
        pass


@api.resource('/notice/<post_id>')
class NoticeAlteration(BaseResource):
    @swag_from(NOTICE_PATCH)
    def patch(self, post_id):
        pass

    @swag_from(NOTICE_DELETE)
    def delete(self, post_id):
        pass
