from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.student import *
from app.models.account import AdminModel, StudentModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/point/student'))


@api.resource('')
class StudentList(BaseResource):
    @auth_required(AdminModel)
    @swag_from(STUDENT_LIST_GET)
    def get(self):
        """
        학생 리스트 조회
        """
        return self.unicode_safe_json_dumps([{
            'id': student.id,
            'name': student.name,
            'number': student.number,
            'goodPoint': student.good_point,
            'badPoint': student.bad_point,
            'penaltyLevel': student.penalty_level,
            'pointHistories': [{
                'time': history.time.strftime('%Y-%m-%d %H:%M:%S'),
                'reason': history.reason,
                'pointType': history.point_type,
                'point': history.point
            } for history in student.point_histories],
            'penaltyTrainingStatus': student.penalty_training_status
        } for student in StudentModel.objects])


@api.resource('/penalty')
class StudentPenalty(BaseResource):
    @swag_from(STUDENT_PENALTY_PATCH)
    def patch(self):
        pass
