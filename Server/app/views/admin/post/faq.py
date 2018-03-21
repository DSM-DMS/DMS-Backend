from datetime import datetime

from flask import Blueprint, Response, g, request
from flask_restful import Api
from flasgger import swag_from

from app.support.resources import BaseResource
from app.support.view_decorators import admin_only

from app.docs.admin.post.faq import *
from app.models.post import FAQModel

api = Api(Blueprint('admin-faq-api', __name__))
api.prefix = '/admin'


@api.resource('/faq')
class FAQManaging(BaseResource):
    @swag_from(FAQ_MANAGING_POST)
    @admin_only
    def post(self):
        """
        FAQ 업로드
        """
        title = request.form['title']
        content = request.form['content']

        admin = g.user
        faq = FAQModel(author=admin.name, title=title, content=content, write_time=datetime.now()).save()

        return self.unicode_safe_json_response({
            'id': str(faq.id)
        }, 201)

    @swag_from(FAQ_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        FAQ 수정
        """
        id = request.form['id']
        title = request.form['title']
        content = request.form['content']

        if len(id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        faq.update(title=title, content=content)

        return Response('', 200)

    @swag_from(FAQ_MANAGING_DELETE)
    @admin_only
    def delete(self):
        """
        FAQ 제거
        """
        id = request.form['id']

        if len(id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        faq.delete()

        return Response('', 200)
