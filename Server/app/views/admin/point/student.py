from datetime import datetime
from bson import ObjectId

from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.support.resources import BaseResource
from app.support.view_decorators import admin_only

from app.docs.admin.point.student import *
from app.models.account import StudentModel
from app.models.point import PointHistoryModel

api = Api(Blueprint('admin-student-point-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/student')
class StudentManaging(BaseResource):
    @swag_from(STUDENT_MANAGING_GET)
    @admin_only
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
            'penalty_level': student.penalty_level,
            'point_histories': [{
                'time': str(history.time)[:-7],
                'reason': history.reason,
                'point_type': history.point_type,
                'point': history.point
            } for history in student.point_histories],
            'penalty_training_status': student.penalty_training_status
        } for student in StudentModel.objects.order_by('number')]

        return self.unicode_safe_json_response(response)


@api.resource('/student/penalty')
class StudentPenaltyManaging(BaseResource):
    @swag_from(STUDENT_PENALTY_MANAGING_PATCH)
    @admin_only
    def patch(self):
        """
        학생 벌점 교육 완료
        """
        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        if not student.penalty_training_status:
            return Response('', 205)

        # 상벌점 삭감
        good_point = student.good_point
        penalty_level = student.penalty_level

        point_decrease = 4 + penalty_level if penalty_level < 4 else 7

        if good_point > point_decrease:
            deleted_point = point_decrease
        else:
            deleted_point = good_point

        student.update(
            good_point=student.good_point - deleted_point,
            bad_point=student.bad_point - deleted_point,
            penalty_training_status=False
        )

        # 상벌점 삭감

        student.point_histories.append(PointHistoryModel(
            reason='벌점 봉사 수료 상점 삭감',
            point_type=True,
            point=-deleted_point,
            time=datetime.now(),
            id=ObjectId()
        ))
        student.point_histories.append(PointHistoryModel(
            reason='벌점 봉사 수료 벌점 삭감',
            point_type=False,
            point=-deleted_point,
            time=datetime.now(),
            id=ObjectId()
        ))
        student.save()

        return Response('', 200)
