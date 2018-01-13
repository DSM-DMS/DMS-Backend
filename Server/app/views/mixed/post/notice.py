import json

from flasgger import swag_from
from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from app.docs.mixed.post.notice import *
from app.models.account import AdminModel, StudentModel
from app.models.post import NoticeModel


class NoticeList(Resource):
    @swag_from(NOTICE_LIST_GET)
    @jwt_required
    def get(self):
        """
        공지사항 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if all((admin, student)):
            return Response('', 403)

        response = [{
            'id': str(notice.id),
            'write_time': str(notice.write_time)[:10],
            'author': notice.author,
            'title': notice.title,
            'pinned': notice.pinned
        } for notice in NoticeModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')


class NoticeItem(Resource):
    @swag_from(NOTICE_ITEM_GET)
    @jwt_required
    def get(self, post_id):
        """
        공지사항 내용 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if all((admin, student)):
            return Response('', 403)

        if len(post_id) != 24:
            return Response('', 204)

        notice = NoticeModel.objects(id=post_id).first()
        if not notice:
            return Response('', 204)

        response = {
            'write_time': str(notice.write_time)[:10],
            'author': notice.author,
            'title': notice.title,
            'content': notice.content,
            'pinned': notice.pinned
        }

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')
