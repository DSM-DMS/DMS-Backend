from flask import Blueprint, Response
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.post.post import *
from app.views.v2 import BaseResource
from app.views.v2.admin.post import CATEGORY_MODEL_MAPPING

api = Api(Blueprint(__name__, __name__))
api.prefix = '/post/<category>'


@api.resource('')
class PostList(BaseResource):
    @swag_from(POST_LIST_GET)
    def get(self, category):
        if category.upper() not in CATEGORY_MODEL_MAPPING:
            self.ValidationError('Invalid category')

        return [{
            'id': str(post.id),
            'writeTime': post.write_time.strftime('%Y-%m-%d'),
            'author': post.author,
            'title': post.title,
            'pinned': post.pinned
        } for post in CATEGORY_MODEL_MAPPING[category.upper()].objects]


@api.resource('/<post_id>')
class PostItem(BaseResource):
    @swag_from(POST_ITEM_GET)
    def get(self, category, post_id):
        if len(post_id) != 24:
            return Response('', 204)

        post = CATEGORY_MODEL_MAPPING[category.upper()].objects(id=post_id).first()

        if not post:
            return Response('', 204)

        return {
            'writeTime': post.write_time.strftime('%Y-%m-%d'),
            'author': post.author,
            'title': post.title,
            'content': post.content,
            'pinned': post.pinned
        }
