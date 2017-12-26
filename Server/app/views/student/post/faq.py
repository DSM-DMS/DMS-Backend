import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.account import StudentModel
from app.models.post import FAQModel


class FAQ(Resource):
    @jwt_required
    def get(self):
        """
        FAQ 리스트 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        return Response(
            json.dumps(
                [{
                    'id': str(faq.id),
                    'write_date': str(faq.write_date),
                    'author': faq.author.name,
                    'title': faq.title,
                    'pinned': faq.pinned
                } for faq in FAQModel.objects],
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )


class FAQItem(Resource):
    @jwt_required
    def get(self):
        """
        FAQ 내용 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        post_id = request.form['post_id']

        faq = FAQModel.objects(id=post_id).first()

        if not faq:
            return Response('', 204)

        return Response(
            json.dumps(
                {
                    'write_date': str(faq.write_date),
                    'author': faq.author.name,
                    'title': faq.title,
                    'content': faq.content,
                    'pinned': faq.pinned
                },
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )
