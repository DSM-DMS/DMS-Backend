from flask import Blueprint
from flask_restful import Api


from app.views.v1 import admin_only
from app.views.v1.admin.post import PostAPIResource


from app.models.post import RuleModel

api = Api(Blueprint('admin-rule-api', __name__))
api.prefix = '/admin'


@api.resource('/rule')
class RuleManaging(PostAPIResource):

    @admin_only
    def post(self):
        """
        기숙사규정 업로드
        """
        return self.upload_post(RuleModel)


    @admin_only
    def patch(self):
        """
        기숙사규정 수정
        """
        return self.modify_post(RuleModel)


    @admin_only
    def delete(self):
        """
        기숙사규정 제거
        """
        return self.delete_post(RuleModel)
