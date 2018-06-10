from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.student import *
from app.models.account import AdminModel, StudentModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/point/student'


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


@api.resource('/penalty/<student_id>')
class StudentPenalty(BaseResource):
    @auth_required(AdminModel)
    @json_required({'status': bool})
    @swag_from(STUDENT_PENALTY_PATCH)
    def patch(self, student_id):
        """
        학생 벌점 교육 상태 변경
        """
        payload = request.json

        status = payload['status']

        student = StudentModel.objects(id=student_id).first()

        if not student:
            return Response('', 204)

        student.update(penalty_training_status=status)

        return Response('', 200)
