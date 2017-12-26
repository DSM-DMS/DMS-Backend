import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.account import StudentModel
from app.models.post import NoticeModel


class Notice(Resource):
    @jwt_required
    def get(self):
        """
        공지사항 리스트 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        return Response(
            json.dumps(
                [{
                    'id': str(notice.id),
                    'write_date': str(notice.write_date),
                    'author': notice.author.name,
                    'title': notice.title,
                    'pinned': notice.pinned
                } for notice in NoticeModel.objects],
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )


class NoticeItem(Resource):
    @jwt_required
    def get(self):
        """
        공지사항 내용 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        post_id = request.form['post_id']

        notice = NoticeModel.objects(id=post_id).first()

        if not notice:
            return Response('', 204)

        return Response(
            json.dumps(
                {
                    'write_date': str(notice.write_date),
                    'author': notice.author.name,
                    'title': notice.title,
                    'content': notice.content,
                    'pinned': notice.pinned
                },
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )
