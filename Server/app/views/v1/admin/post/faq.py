from flask import Blueprint
from flask_restful import Api


from app.views.v1 import admin_only
from app.views.v1.admin.post import PostAPIResource


from app.models.post import FAQModel

api = Api(Blueprint('admin-faq-api', __name__))
api.prefix = '/admin'


@api.resource('/faq')
class FAQManaging(PostAPIResource):

    @admin_only
    def post(self):
        """
        FAQ 업로드
        """
        return self.upload_post(FAQModel)


    @admin_only
    def patch(self):
        """
        FAQ 수정
        """
        return self.modify_post(FAQModel)


    @admin_only
    def delete(self):
        """
        FAQ 제거
        """
        return self.delete_post(FAQModel)
