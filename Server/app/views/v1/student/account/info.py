from flask import Blueprint, g
from flask_restful import Api


from app.views.v1 import BaseResource
from app.views.v1 import student_only


from app.models.apply import *

api = Api(Blueprint('student-info-api', __name__))


@api.resource('/mypage')
class MyPage(BaseResource):

    @student_only
    def get(self):
        """
        마이페이지에 해당하는 정보 조회
        """
        student = g.user

        extension_11 = ExtensionApply11Model.objects(student=student).first()
        extension_12 = ExtensionApply12Model.objects(student=student).first()
        goingout = GoingoutApplyModel.objects(student=student).first()
        stay = StayApplyModel.objects(student=student).first()

        response = {
            'name': student.name,
            'number': student.number,

            'extension_11': {
                'class_num': extension_11.class_,
                'seat_num': extension_11.seat
            } if extension_11 else None,

            'extension_12': {
                'class_num': extension_12.class_,
                'seat_num': extension_12.seat
            } if extension_12 else None,

            'goingout': {
                'sat': goingout.on_saturday,
                'sun': goingout.on_sunday
            },
            'stay_value': stay.value,
            'good_point': student.good_point,
            'bad_point': student.bad_point
        }

        return self.unicode_safe_json_response(response)


@api.resource('/point/history')
class PointHistory(BaseResource):

    @student_only
    def get(self):
        """
        자신의 상벌점 부여 내역 조회
        """
        student = g.user

        response = [{
            'time': str(history.time)[:10],
            'reason': history.reason,
            'point_type': history.point_type,
            'point': history.point
        } for history in student.point_histories]

        return self.unicode_safe_json_response(response)
