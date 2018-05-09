from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.rule import *
from app.models.account import AdminModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/point'))


@api.resource('/rule')
class Rule(BaseResource):
    @auth_required(AdminModel)
    @swag_from(RULE_GET)
    def get(self):
        """
        상벌점 규칙 목록 조회
        """

    @auth_required(AdminModel)
    @swag_from(RULE_POST)
    def post(self):
        """
        상벌점 규칙 추가
        """


@api.resource('/rule/<rule_id>')
class RuleAlteration(BaseResource):
    @auth_required(AdminModel)
    @swag_from(RULE_ALTERATION_PATCH)
    def patch(self):
        """
        상벌점 규칙 내용 수정
        """

    @auth_required(AdminModel)
    @swag_from(RULE_ALTERATION_DELETE)
    def delete(self):
        """
        상벌점 규칙 삭제
        """
