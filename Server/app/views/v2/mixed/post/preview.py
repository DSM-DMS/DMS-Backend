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
        if category.upper() not in CATEGORY_MODEL_MAPPING:
            self.ValidationError('Invalid category')

        model = CATEGORY_MODEL_MAPPING[category.upper()]

        post = model.objects(pinned=True).first()

        if not post:
            post = model.objects.first()

            if not post:
                return Response('', 204)

        return {
            'writeTime': post.write_time.strftime('%Y-%m-%d'),
            'author': post.author,
            'title': post.title,
            'content': post.content
        }
