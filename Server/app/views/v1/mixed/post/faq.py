from flasgger import swag_from
from flask import Blueprint
from flask_restful import Api

from app.views.v1 import auth_required

from app.docs.v1.mixed.post.faq import *
from app.models.v2.post import FAQModel
from app.views.v1.mixed.post import PostAPIResource

api = Api(Blueprint('faq-api', __name__))


@api.resource('/faq')
class FAQList(PostAPIResource):
    @swag_from(FAQ_LIST_GET)
    @auth_required
    def get(self):
        """
        FAQ 리스트 조회
        """
        return self.get_list_as_response(FAQModel)


@api.resource('/faq/<post_id>')
class FAQItem(PostAPIResource):
    @swag_from(FAQ_ITEM_GET)
    @auth_required
    def get(self, post_id):
        """
        FAQ 내용 조회
        """
        return self.get_item_as_response(FAQModel, post_id)
