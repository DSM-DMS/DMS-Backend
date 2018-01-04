import json

from flasgger import swag_from
from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from app.docs.mixed.post.faq import *
from app.models.account import AdminModel, StudentModel
from app.models.post import FAQModel


class FAQList(Resource):
    @swag_from(FAQ_LIST_GET)
    @jwt_required
    def get(self):
        """
        FAQ 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not any((admin, student)):
            return Response('', 403)

        response = [{
            'id': str(faq.id),
            'write_time': str(faq.write_time)[:-7],
            'author': faq.author,
            'title': faq.title,
            'pinned': faq.pinned
        } for faq in FAQModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')


class FAQItem(Resource):
    @swag_from(FAQ_ITEM_GET)
    @jwt_required
    def get(self, post_id):
        """
        FAQ 내용 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not any((admin, student)):
            return Response('', 403)

        if len(post_id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=post_id).first()
        if not faq:
            return Response('', 204)

        response = {
            'write_time': str(faq.write_time)[:-7],
            'author': faq.author,
            'title': faq.title,
            'content': faq.content,
            'pinned': faq.pinned
        }

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')
