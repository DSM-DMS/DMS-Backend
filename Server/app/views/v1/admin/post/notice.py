from flask import Blueprint
from flask_restful import Api


from app.views.v1 import admin_only
from app.views.v1.admin.post import PostAPIResource


from app.models.post import NoticeModel

api = Api(Blueprint('admin-notice-api', __name__))
api.prefix = '/admin'


@api.resource('/notice')
class NoticeManaging(PostAPIResource):
    
    @admin_only
    def post(self):
        """
        공지사항 업로드
        """
        return self.upload_post(NoticeModel)

    
    @admin_only
    def patch(self):
        """
        공지사항 수정
        """
        return self.modify_post(NoticeModel)

    
    @admin_only
    def delete(self):
        """
        공지사항 제거
        """
        return self.delete_post(NoticeModel)
