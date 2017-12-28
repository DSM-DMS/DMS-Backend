from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.admin.post.preview import *
from app.models.account import AdminModel
from app.models.post import FAQModel, NoticeModel, RuleModel


class FAQPreviewManaging(Resource):
    @swag_from(FAQ_PREVIEW_POST)
    @jwt_required
    def post(self):
        """
        FAQ 프리뷰 설정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form.get('id')

        pinned_faq = FAQModel.objects(pinned=True).first()
        if pinned_faq:
            pinned_faq.update(pinned=False)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        faq.update(pinned=True)

        return Response('', 201)


class NoticePreviewManaging(Resource):
    @swag_from(NOTICE_PREVIEW_POST)
    @jwt_required
    def post(self):
        """
        공지사항 프리뷰 설정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form.get('id')

        pinned_notice = NoticeModel.objects(pinned=True).first()
        if pinned_notice:
            pinned_notice.update(pinned=False)

        notice = NoticeModel.objects(id=id).first()
        if not notice:
            return Response('', 204)

        notice.update(pinned=True)

        return Response('', 201)


class RulePreviewManaging(Resource):
    @swag_from(RULE_PREVIEW_POST)
    @jwt_required
    def post(self):
        """
        기숙사규정 프리뷰 설정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form.get('id')

        pinned_rule = RuleModel.objects(pinned=True).first()
        if pinned_rule:
            pinned_rule.update(pinned=False)

        rule = RuleModel.objects(id=id).first()
        if not rule:
            return Response('', 204)

        rule.update(pinned=True)

        return Response('', 201)
