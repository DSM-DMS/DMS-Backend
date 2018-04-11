from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views.v1 import admin_only
from app.views.v1.admin.post import PostAPIResource

from app.docs.v1.admin.post.notice import *
from app.models.v2.post import NoticeModel

api = Api(Blueprint('admin-notice-api', __name__))
api.prefix = '/admin'


@api.resource('/notice')
class NoticeManaging(PostAPIResource):
    @swag_from(NOTICE_MANAGING_POST)
    @admin_only
    def post(self):
        """
        공지사항 업로드
        """
        return self.upload_post(NoticeModel)

    @swag_from(NOTICE_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        공지사항 수정
        """
        return self.modify_post(NoticeModel)

    @swag_from(NOTICE_MANAGING_DELETE)
    @admin_only
    def delete(self):
        """
        공지사항 제거
        """
        return self.delete_post(NoticeModel)