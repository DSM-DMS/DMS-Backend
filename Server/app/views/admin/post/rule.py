from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.admin.post.rule import *
from app.models.account import AdminModel
from app.models.post import RuleModel
from app.views import BaseResource

api = Api(Blueprint('admin-rule-api', __name__))
api.prefix = '/admin'


@api.resource('/rule')
class RuleManaging(BaseResource):
    @swag_from(RULE_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        기숙사규정 업로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        title = request.form['title']
        content = request.form['content']

        rule = RuleModel(author=admin.name, title=title, content=content).save()

        return self.unicode_safe_json_response({
            'id': str(rule.id)
        }, 201)

    @swag_from(RULE_MANAGING_PATCH)
    @jwt_required
    def patch(self):
        """
        기숙사규정 수정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        id = request.form['id']
        title = request.form['title']
        content = request.form['content']

        if len(id) != 24:
            return Response('', 204)

        rule = RuleModel.objects(id=id).first()
        if not rule:
            return Response('', 204)

        rule.update(title=title, content=content)

        return Response('', 200)

    @swag_from(RULE_MANAGING_DELETE)
    @jwt_required
    def delete(self):
        """
        기숙사규정 제거
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        id = request.form['id']

        if len(id) != 24:
            return Response('', 204)

        rule = RuleModel.objects(id=id).first()
        if not rule:
            return Response('', 204)

        rule.delete()

        return Response('', 200)

