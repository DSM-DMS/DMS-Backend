from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.post.notice import *
from app.models.account import AdminModel
from app.models.post import NoticeModel
from app.views import BaseResource

api = Api(Blueprint('admin-notice-api', __name__))
api.prefix = '/admin'


@api.resource('/notice')
class NoticeManaging(BaseResource):
    @swag_from(NOTICE_MANAGING_POST)
    @BaseResource.admin_only
    def post(self):
        """
        공지사항 업로드
        """
        title = request.form['title']
        content = request.form['content']

        admin = AdminModel.objects(id=get_jwt_identity()).first()
        notice = NoticeModel(author=admin.name, title=title, content=content).save()

        return self.unicode_safe_json_response({
            'id': str(notice.id)
        }, 201)

    @swag_from(NOTICE_MANAGING_PATCH)
    @BaseResource.admin_only
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
    @BaseResource.admin_only
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
