from flask import Blueprint, Response
from flask_jwt_extended import jwt_required
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.point.rule import *
from app.models.point import PointRuleModel
from app.views import BaseResource

api = Api(Blueprint('admin-point-rule-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/rule')
class PointRuleManaging(BaseResource):
    @swag_from(POINT_RULE_MANAGING_GET)
    @jwt_required
    @BaseResource.admin_only
    def get(self):
        """
        상벌점 규칙 목록 조회
        """
        response = [{
            'id': str(rule.id),
            'name': rule.name,
            'min_point': rule.min_point,
            'max_point': rule.max_point
        } for rule in PointRuleModel.objects]

        return self.unicode_safe_json_response(response)

    @swag_from(POINT_RULE_MANAGING_POST)
    @jwt_required
    @BaseResource.admin_only
    def post(self):
        """
        상벌점 규칙 추가
        """
        name = request.form['name']
        min_point = int(request.form['min_point'])
        max_point = int(request.form['max_point'])

        rule = PointRuleModel(
            name=name,
            min_point=min_point,
            max_point=max_point
        ).save()

        return {
            'id': str(rule.id)
        }, 201

    @swag_from(POINT_RULE_MANAGING_PATCH)
    @jwt_required
    @BaseResource.admin_only
    def patch(self):
        """
        상벌점 규칙 수정
        """
        rule_id = request.form['rule_id']
        if len(rule_id) != 24:
            return Response('', 204)

        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 204)

        name = request.form['name']
        min_point = int(request.form['min_point'])
        max_point = int(request.form['max_point'])

        rule.update(
            name=name,
            min_point=min_point,
            max_point=max_point
        )

        return Response('', 200)

    @swag_from(POINT_RULE_MANAGING_DELETE)
    @jwt_required
    @BaseResource.admin_only
    def delete(self):
        """
        상벌점 규칙 삭제
        """
        rule_id = request.form['rule_id']
        if len(rule_id) != 24:
            return Response('', 204)

        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 204)

        rule.delete()

        return Response('', 200)
