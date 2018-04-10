from flasgger import swag_from
from flask import Blueprint
from flask_restful import Api

from app_v1.views import auth_required

from app_v1.docs.mixed.post.rule import *
from app_v2.models.post import RuleModel
from app_v1.views.mixed.post import PostAPIResource

api = Api(Blueprint('rule-api', __name__))


@api.resource('/rule')
class RuleList(PostAPIResource):
    @swag_from(RULE_LIST_GET)
    @auth_required
    def get(self):
        """
        기숙사규칙 리스트 조회
        """
        return self.get_list_as_response(RuleModel)


@api.resource('/rule/<post_id>')
class RuleItem(PostAPIResource):
    @swag_from(RULE_ITEM_GET)
    @auth_required
    def get(self, post_id):
        """
        기숙사규칙 내용 조회
        """
        return self.get_item_as_response(RuleModel, post_id)
