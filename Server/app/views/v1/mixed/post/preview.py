
from flask import Blueprint
from flask_restful import Api

from app.views.v1 import auth_required


from app.models.post import FAQModel, NoticeModel, RuleModel
from app.views.v1.mixed.post import PostAPIResource

api = Api(Blueprint('preview-api', __name__))


@api.resource('/preview/faq')
class FAQPreview(PostAPIResource):

    @auth_required
    def get(self):
        """
        FAQ 프리뷰 조회
        """
        return self.get_preview_item_as_response(FAQModel)


@api.resource('/preview/notice')
class NoticePreview(PostAPIResource):

    @auth_required
    def get(self):
        """
        공지사항 프리뷰 조회
        """
        return self.get_preview_item_as_response(NoticeModel)


@api.resource('/preview/rule')
class RulePreview(PostAPIResource):

    @auth_required
    def get(self):
        """
        기숙사규정 프리뷰 조회
        """
        return self.get_preview_item_as_response(RuleModel)
