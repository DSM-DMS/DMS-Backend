from flasgger import swag_from
from flask import Blueprint, Response
from flask_restful import Api

from app.docs.mixed.post.preview import *
from app.models.post import FAQModel, NoticeModel, RuleModel
from app.views import BaseResource

from utils.access_controller import signed_account_only

api = Api(Blueprint('preview-api', __name__))


@api.resource('/preview/faq')
class FAQPreview(BaseResource):
    @swag_from(FAQ_PREVIEW_GET)
    @signed_account_only
    def get(self):
        """
        FAQ 프리뷰 조회
        """
        faq = FAQModel.objects(pinned=True).first()
        if not faq:
            faq = FAQModel.objects().first()
            if not faq:
                return Response('', 204)

        response = {
            'write_time': str(faq.write_time)[:10],
            'author': faq.author,
            'title': faq.title,
            'content': faq.content,
            'pinned': faq.pinned
        }

        return self.unicode_safe_json_response(response)


@api.resource('/preview/notice')
class NoticePreview(BaseResource):
    @swag_from(NOTICE_PREVIEW_GET)
    @signed_account_only
    def get(self):
        """
        공지사항 프리뷰 조회
        """
        notice = NoticeModel.objects(pinned=True).first()
        if not notice:
            notice = NoticeModel.objects().first()
            if not notice:
                return Response('', 204)

        response ={
            'write_time': str(notice.write_time)[:10],
            'author': notice.author,
            'title': notice.title,
            'content': notice.content,
            'pinned': notice.pinned
        }

        return self.unicode_safe_json_response(response)


@api.resource('/preview/rule')
class RulePreview(BaseResource):
    @swag_from(RULE_PREVIEW_GET)
    @signed_account_only
    def get(self):
        """
        기숙사규정 프리뷰 조회
        """
        rule = RuleModel.objects(pinned=True).first()
        if not rule:
            rule = RuleModel.objects().first()
            if not rule:
                return Response('', 204)

        response = {
            'write_time': str(rule.write_time)[:10],
            'author': rule.author,
            'title': rule.title,
            'content': rule.content,
            'pinned': rule.pinned
        }

        return self.unicode_safe_json_response(response)
