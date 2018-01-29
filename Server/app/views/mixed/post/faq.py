import json

from flasgger import swag_from
from flask import Blueprint, Response
from flask_jwt_extended import jwt_required
from flask_restful import Api

from app.docs.mixed.post.faq import *
from app.models.post import FAQModel
from app.views import BaseResource

from utils.access_controller import signed_account_only

api = Api(Blueprint('faq-api', __name__))


@api.resource('/faq')
class FAQList(BaseResource):
    @swag_from(FAQ_LIST_GET)
    @signed_account_only
    def get(self):
        """
        FAQ 리스트 조회
        """
        response = [{
            'id': str(faq.id),
            'write_time': str(faq.write_time)[:10],
            'author': faq.author,
            'title': faq.title,
            'pinned': faq.pinned
        } for faq in FAQModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), content_type='application/json; charset=utf8')


@api.resource('/faq/<post_id>')
class FAQItem(BaseResource):
    @swag_from(FAQ_ITEM_GET)
    @jwt_required
    def get(self, post_id):
        """
        FAQ 내용 조회
        """
        if len(post_id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=post_id).first()
        if not faq:
            return Response('', 204)

        response = {
            'write_time': str(faq.write_time)[:10],
            'author': faq.author,
            'title': faq.title,
            'content': faq.content,
            'pinned': faq.pinned
        }

        return Response(json.dumps(response, ensure_ascii=False), content_type='application/json; charset=utf8')
