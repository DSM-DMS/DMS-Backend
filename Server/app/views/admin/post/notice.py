from datetime import datetime

from flask import Blueprint, Response, g, request
from flask_restful import Api
from flasgger import swag_from

from app.support.resources import BaseResource
from app.support.view_decorators import admin_only

from app.docs.admin.post.notice import *
from app.models.post import NoticeModel

api = Api(Blueprint('admin-notice-api', __name__))
api.prefix = '/admin'


@api.resource('/notice')
class NoticeManaging(BaseResource):
    @swag_from(NOTICE_MANAGING_POST)
    @admin_only
    def post(self):
        """
        공지사항 업로드
        """
        title = request.form['title']
        content = request.form['content']

        admin = g.user
        notice = NoticeModel(author=admin.name, title=title, content=content, write_time=datetime.now()).save()

        return self.unicode_safe_json_response({
            'id': str(notice.id)
        }, 201)

    @swag_from(NOTICE_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        공지사항 수정
        """
        id = request.form['id']
        title = request.form['title']
        content = request.form['content']

        if len(id) != 24:
            return Response('', 204)

        notice = NoticeModel.objects(id=id).first()
        if not notice:
            return Response('', 204)

        notice.update(title=title, content=content)

        return Response('', 200)

    @swag_from(NOTICE_MANAGING_DELETE)
    @admin_only
    def delete(self):
        """
        공지사항 제거
        """
        id = request.form['id']

        if len(id) != 24:
            return Response('', 204)

        notice = NoticeModel.objects(id=id).first()
        if not notice:
            return Response('', 204)

        notice.delete()

        return Response('', 200)
