from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Api
from flasgger import swag_from

from app.docs.admin.point.student import *
from app.models.account import StudentModel
from app.views import BaseResource

api = Api(Blueprint('admin-student-point-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/student')
class StudentManaging(BaseResource):
    @swag_from(STUDENT_MANAGING_GET)
    @jwt_required
    @BaseResource.admin_only
    def get(self):
        """
        학생 목록 조회
        """
        response = [{
            'id': student.id,
            'name': student.name,
            'number': student.number,
            'good_point': student.good_point,
            'bad_point': student.bad_point,
            'point_histories': [{
                'time': str(history.time)[:-7],
                'reason': history.reason,
                'point': history.point
            } for history in student.point_histories],
            'penalty_training_status': student.penalty_training_status
        } for student in StudentModel.objects.order_by('number')]

        return self.unicode_safe_json_response(response)
