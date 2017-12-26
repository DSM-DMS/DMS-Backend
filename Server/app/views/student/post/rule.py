import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.post.rule import *
from app.models.account import StudentModel
from app.models.post import RuleModel


class RuleList(Resource):
    @swag_from(RULE_LIST_GET)
    @jwt_required
    def get(self):
        """
        기숙사규칙 리스트 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        return Response(
            json.dumps(
                [{
                    'id': str(rule.id),
                    'write_date': str(rule.write_date),
                    'author': rule.author.name,
                    'title': rule.title,
                    'pinned': rule.pinned
                } for rule in RuleModel.objects],
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )


class RuleItem(Resource):
    @swag_from(RULE_ITEM_GET)
    @jwt_required
    def get(self):
        """
        기숙사규칙 내용 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        post_id = request.form['post_id']

        rule = RuleModel.objects(id=post_id).first()

        if not rule:
            return Response('', 204)

        return Response(
            json.dumps(
                {
                    'write_date': str(rule.write_date),
                    'author': rule.author.name,
                    'title': rule.title,
                    'content': rule.content,
                    'pinned': rule.pinned
                },
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )
