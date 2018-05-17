from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.preview import *
from app.models.account import AdminModel
from app.views.v2 import BaseResource, auth_required, json_required_2
from app.views.v2.admin.post import CATEGORY_MODEL_MAPPING

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/post-preview/<category>'


@api.resource('')
class Preview(BaseResource):
    @auth_required(AdminModel)
    @json_required_2({'id': str})
    @swag_from(PREVIEW_PATCH)
    def patch(self, category):
        """
        게시글 프리뷰 설정
        """
        id = request.json['id']

        if category.upper() not in CATEGORY_MODEL_MAPPING:
            self.ValidationError('Invalid category')

        if len(id) != 24:
            return Response('', 204)

        post = CATEGORY_MODEL_MAPPING[category.upper()].objects(id=id).first()

        if not post:
            return Response('', 204)

        pinned_post = CATEGORY_MODEL_MAPPING[category.upper()].objects(pinned=True).first()

        if pinned_post:
            pinned_post.update(pinned=False)

        updated = post.update(pinned=True)

        if updated:
            return Response('', 200)
        else:
            abort(500)
