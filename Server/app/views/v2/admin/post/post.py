from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.post import *
from app.models.account import AdminModel
from app.models.post import FAQModel, NoticeModel, RuleModel
from app.views.v2 import BaseResource, auth_required, json_required


CATEGORY_MODEL_MAPPING = {
    'FAQ': FAQModel,
    'NOTICE': NoticeModel,
    'RULE': RuleModel
}
api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/post'


@api.resource('/<category>')
class Post(BaseResource):
    @auth_required(AdminModel)
    @swag_from(POST_POST)
    def post(self, category):
        """
        게시글 업로드
        """
        title = request.json['title']
        content = request.json['content']

        if category.upper() not in CATEGORY_MODEL_MAPPING:
            abort(400)

        post = CATEGORY_MODEL_MAPPING[category.upper()](
            author=g.user.name,
            title=title,
            content=content
        ).save()

        return {
            'id': str(post.id)
        }, 201


@api.resource('/<category>/<post_id>')
class PostAlteration(BaseResource):
    @auth_required(AdminModel)
    @swag_from(POST_PATCH)
    def patch(self, category, post_id):
        """
        게시글 수정
        """
        title = request.json['title']
        content = request.json['content']

        if category.upper() not in CATEGORY_MODEL_MAPPING:
            abort(400)

        if len(post_id) != 24:
            return Response('', 204)

        post = CATEGORY_MODEL_MAPPING[category.upper()].objects(id=post_id).first()

        if not post:
            return Response('', 204)

        updated = post.update(
            title=title,
            content=content
        )

        if updated:
            return Response('', 200)
        else:
            abort(500)

    @auth_required(AdminModel)
    @swag_from(POST_DELETE)
    def delete(self, category, post_id):
        """
        게시글 삭제
        """
        if category.upper() not in CATEGORY_MODEL_MAPPING:
            abort(400)

        if len(post_id) != 24:
            return Response('', 204)

        post = CATEGORY_MODEL_MAPPING[category.upper()].objects(id=post_id).first()

        if not post:
            return Response('', 204)

        post.delete()

        return Response('', 200)
