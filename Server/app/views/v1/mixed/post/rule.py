
from flask import Blueprint
from flask_restful import Api

from app.views.v1 import auth_required


from app.models.post import RuleModel
from app.views.v1.mixed.post import PostAPIResource

api = Api(Blueprint('rule-api', __name__))


@api.resource('/rule')
class RuleList(PostAPIResource):

    @auth_required
    def get(self):
        """
        기숙사규칙 리스트 조회
        """
        return self.get_list_as_response(RuleModel)


@api.resource('/rule/<post_id>')
class RuleItem(PostAPIResource):

    @auth_required
    def get(self, post_id):
        """
        기숙사규칙 내용 조회
        """
        return self.get_item_as_response(RuleModel, post_id)
