from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.point import *
from app.models.account import AdminModel, StudentModel
from app.models.point import PointRuleModel, PointHistoryModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin'))


@api.resource('/point')
class Point(BaseResource):
    @auth_required(AdminModel)
    @swag_from(POINT_GET)
    def get(self):
        """
        특정 학생의 상벌점 내역 조회
        """
        id = request.args['id']

        student = StudentModel.objects(id=id).first()

        if not student:
            return Response('', 204)

        return self.unicode_safe_json_dumps([{
            'id': str(history.id),
            'date': history.time.strftime('%Y-%m-%d'),
            'reason': history.reason,
            'pointType': history.point_type,
            'point': history.point
        } for history in student.point_histories])

    @swag_from(POINT_POST)
    def post(self):
        pass

    @swag_from(POINT_DELETE)
    def patch(self):
        pass
