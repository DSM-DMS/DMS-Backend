from flasgger import swag_from
from flask import Blueprint, Response
from flask_jwt_extended import jwt_required
from flask_restful import Api

from app.docs.mixed.post.notice import *
from app.models.post import NoticeModel
from app.views import BaseResource

api = Api(Blueprint('notice-api', __name__))


@api.resource('/notice')
class NoticeList(BaseResource):
    @swag_from(NOTICE_LIST_GET)
    @jwt_required
    @BaseResource.signed_account_only
    def get(self):
        """
        공지사항 리스트 조회
        """
        response = [{
            'id': str(notice.id),
            'write_time': str(notice.write_time)[:10],
            'author': notice.author,
            'title': notice.title,
            'pinned': notice.pinned
        } for notice in NoticeModel.objects]

        return self.unicode_safe_json_response(response)


@api.resource('/notice/<post_id>')
class NoticeItem(BaseResource):
    @swag_from(NOTICE_ITEM_GET)
    @jwt_required
    @BaseResource.signed_account_only
    def get(self, post_id):
        """
        공지사항 내용 조회
        """
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

        return self.unicode_safe_json_response(response)
