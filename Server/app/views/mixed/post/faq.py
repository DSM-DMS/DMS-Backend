from flasgger import swag_from
from flask import Blueprint, Response
from flask_restful import Api

from app.docs.mixed.post.faq import *
from app.models.support.mongo_helper import mongo_to_dict
from app.models.post import FAQModel
from app.support.resources import BaseResource
from app.support.view_decorators import auth_required

api = Api(Blueprint('faq-api', __name__))


@api.resource('/faq')
class FAQList(BaseResource):
    @swag_from(FAQ_LIST_GET)
    @auth_required
    def get(self):
        """
        FAQ 리스트 조회
        """
        response = [mongo_to_dict(faq, ['content']) for faq in FAQModel.objects]

        return self.unicode_safe_json_response(response)


@api.resource('/faq/<post_id>')
class FAQItem(BaseResource):
    @swag_from(FAQ_ITEM_GET)
    @auth_required
    def get(self, post_id):
        """
        FAQ 내용 조회
        """
        if len(post_id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=post_id).first()
        if not faq:
            return Response('', 204)

        response = mongo_to_dict(faq, ['id'])

        return self.unicode_safe_json_response(response)
