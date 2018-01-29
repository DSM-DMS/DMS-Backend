from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, Resource, abort, request
from flasgger import swag_from

from app.docs.admin.post.faq import *
from app.models.account import AdminModel
from app.models.post import FAQModel

api = Api(Blueprint('admin-faq-api', __name__))
api.prefix = '/admin'


@api.resource('/faq')
class FAQManaging(Resource):
    @swag_from(FAQ_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        FAQ 업로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        title = request.form['title']
        content = request.form['content']

        faq = FAQModel(author=admin.name, title=title, content=content).save()

        return {
            'id': str(faq.id)
        }, 201

    @swag_from(FAQ_MANAGING_PATCH)
    @jwt_required
    def patch(self):
        """
        FAQ 수정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

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
    @jwt_required
    def delete(self):
        """
        FAQ 제거
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        id = request.form['id']

        if len(id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        faq.delete()

        return Response('', 200)
