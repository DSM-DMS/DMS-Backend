from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.views import admin_only

from app.docs.admin.point.rule import *

from app.models.support.mongo_helper import mongo_to_dict
from app.models.point import PointRuleModel

api = Api(Blueprint('admin-point-rule-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/rule')
class PointRuleManaging(BaseResource):
    @swag_from(POINT_RULE_MANAGING_GET)
    @admin_only
    def get(self):
        """
        상벌점 규칙 목록 조회
        """
        response = [mongo_to_dict(rule) for rule in PointRuleModel.objects]

        return self.unicode_safe_json_response(response)

    @swag_from(POINT_RULE_MANAGING_POST)
    @admin_only
    def post(self):
        """
        상벌점 규칙 추가
        """
        name = request.form['name']
        point_type = request.form['point_type'].upper() == 'TRUE'
        min_point = int(request.form['min_point'])
        max_point = int(request.form['max_point'])

        rule = PointRuleModel(
            name=name,
            point_type=point_type,
            min_point=min_point,
            max_point=max_point
        ).save()

        return {
            'id': str(rule.id)
        }, 201

    @swag_from(POINT_RULE_MANAGING_PATCH)
    @admin_only
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
        point_type = request.form['point_type'].upper() == 'TRUE'
        min_point = int(request.form['min_point'])
        max_point = int(request.form['max_point'])

        rule.update(
            name=name,
            point_type=point_type,
            min_point=min_point,
            max_point=max_point
        )

        return Response('', 200)

    @swag_from(POINT_RULE_MANAGING_DELETE)
    @admin_only
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
