from flask import Blueprint, Response, request
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
            'bad_point_status': student.bad_point_status,
            'point_histories': [{
                'time': str(history.time)[:-7],
                'reason': history.reason,
                'point': history.point
            } for history in student.point_histories],
            'penalty_trained': student.penalty_trained
        } for student in StudentModel.objects.order_by('number')]

        return self.unicode_safe_json_response(response)


@api.resource('/student/penalty')
class StudentPenaltyManaging(BaseResource):
    @swag_from(STUDENT_PENALTY_MANAGING_PATCH)
    @BaseResource.admin_only
    def patch(self):
        """
        학생 벌점 교육 상태 변경
        """
        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        status = request.form['status'].upper() == 'TRUE'

        student.update(penalty_trained=status)

        if not status:
            good_point = student.good_point
            if good_point > 4:
                bad_point = student.bad_point - 5
                good_point -= 5
            else:
                bad_point = student.bad_point - good_point
                good_point = 0

            student.update(bad_point=bad_point, good_point=good_point)

        return Response('', 200)
