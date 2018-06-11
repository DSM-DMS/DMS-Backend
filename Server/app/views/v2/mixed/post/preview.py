from flask import Blueprint, Response
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.post.preview import *
from app.views.v2 import BaseResource
from app.views.v2.admin.post import CATEGORY_MODEL_MAPPING

api = Api(Blueprint(__name__, __name__))
api.prefix = '/post-preview/<category>'


@api.resource('')
class FAQPreview(BaseResource):
    @swag_from(PREVIEW_GET)
    def get(self, category):
        """
        특정 카테고리의 고정 게시글 조회
        """
        if category.upper() not in CATEGORY_MODEL_MAPPING:
            raise self.ValidationError('Invalid category')

        model = CATEGORY_MODEL_MAPPING[category.upper()]

        post = model.objects(pinned=True).first() or model.objects.first()

        return {
            'writeTime': post.write_time.strftime('%Y-%m-%d'),
            'author': post.author,
            'title': post.title,
            'content': post.content
        } if post else Response('', 204)
