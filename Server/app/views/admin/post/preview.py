from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.admin.post.preview import *
from app.models.post import FAQModel, NoticeModel, RuleModel
from app.support.resources import BaseResource
from app.support.view_decorators import admin_only

api = Api(Blueprint('admin-preview-api', __name__))
api.prefix = '/admin/preview'


@api.resource('/faq')
class FAQPreviewManaging(BaseResource):
    @swag_from(FAQ_PREVIEW_MANAGING_POST)
    @admin_only
    def post(self):
        """
        FAQ 프리뷰 설정
        """
        id = request.form.get('id')
        if len(id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        pinned_faq = FAQModel.objects(pinned=True).first()
        if pinned_faq:
            pinned_faq.update(pinned=False)

        faq.update(pinned=True)

        return Response('', 201)


@api.resource('/notice')
class NoticePreviewManaging(BaseResource):
    @swag_from(NOTICE_PREVIEW_MANAGING_POST)
    @admin_only
    def post(self):
        """
        공지사항 프리뷰 설정
        """
        id = request.form.get('id')
        if len(id) != 24:
            return Response('', 204)

        notice = NoticeModel.objects(id=id).first()
        if not notice:
            return Response('', 204)

        pinned_notice = NoticeModel.objects(pinned=True).first()
        if pinned_notice:
            pinned_notice.update(pinned=False)

        notice.update(pinned=True)

        return Response('', 201)


@api.resource('/rule')
class RulePreviewManaging(BaseResource):
    @swag_from(RULE_PREVIEW_MANAGING_POST)
    @admin_only
    def post(self):
        """
        기숙사규정 프리뷰 설정
        """
        id = request.form.get('id')
        if len(id) != 24:
            return Response('', 204)

        rule = RuleModel.objects(id=id).first()
        if not rule:
            return Response('', 204)

        pinned_rule = RuleModel.objects(pinned=True).first()
        if pinned_rule:
            pinned_rule.update(pinned=False)

        rule.update(pinned=True)

        return Response('', 201)
