from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views.v1 import admin_only
from app.views.v1.admin.post import PostAPIResource

from app.docs.v1.admin.post.faq import *
from app.models.post import FAQModel

api = Api(Blueprint('admin-faq-api', __name__))
api.prefix = '/admin'


@api.resource('/faq')
class FAQManaging(PostAPIResource):
    @swag_from(FAQ_MANAGING_POST)
    @admin_only
    def post(self):
        """
        FAQ 업로드
        """
        return self.upload_post(FAQModel)

    @swag_from(FAQ_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        FAQ 수정
        """
        return self.modify_post(FAQModel)

    @swag_from(FAQ_MANAGING_DELETE)
    @admin_only
    def delete(self):
        """
        FAQ 제거
        """
        return self.delete_post(FAQModel)
