from datetime import datetime

from flask import Blueprint, Response, g, request
from flask_restful import Api
from flasgger import swag_from

from app.support.resources import BaseResource
from app.support.view_decorators import admin_only

from app.docs.admin.post.rule import *
from app.models.post import RuleModel

api = Api(Blueprint('admin-rule-api', __name__))
api.prefix = '/admin'


@api.resource('/rule')
class RuleManaging(BaseResource):
    @swag_from(RULE_MANAGING_POST)
    @admin_only
    def post(self):
        """
        기숙사규정 업로드
        """
        title = request.form['title']
        content = request.form['content']

        admin = g.user
        rule = RuleModel(author=admin.name, title=title, content=content, write_time=datetime.now()).save()

        return self.unicode_safe_json_response({
            'id': str(rule.id)
        }, 201)

    @swag_from(RULE_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        기숙사규정 수정
        """
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
    @admin_only
    def delete(self):
        """
        기숙사규정 제거
        """
        id = request.form['id']

        if len(id) != 24:
            return Response('', 204)

        rule = RuleModel.objects(id=id).first()
        if not rule:
            return Response('', 204)

        rule.delete()

        return Response('', 200)

