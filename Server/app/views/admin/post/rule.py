from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views import admin_only
from app.views.admin.post import PostAPIResource

from app.docs.admin.post.rule import *
from app.models.post import RuleModel

api = Api(Blueprint('admin-rule-api', __name__))
api.prefix = '/admin'


@api.resource('/rule')
class RuleManaging(PostAPIResource):
    @swag_from(RULE_MANAGING_POST)
    @admin_only
    def post(self):
        """
        기숙사규정 업로드
        """
        return self.upload_post(RuleModel)

    @swag_from(RULE_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        기숙사규정 수정
        """
        return self.modify_post(RuleModel)

    @swag_from(RULE_MANAGING_DELETE)
    @admin_only
    def delete(self):
        """
        기숙사규정 제거
        """
        return self.delete_post(RuleModel)
