from flask import Blueprint, g
from flask_restful import Api
from flasgger import swag_from

from app.support.resources import BaseResource
from app.support.view_decorators import student_only

from app.docs.student.account.info import *

api = Api(Blueprint('student-info-api', __name__))


@api.resource('/mypage')
class MyPage(BaseResource):
    @swag_from(MYPAGE_GET)
    @student_only
    def get(self):
        """
        마이페이지에 해당하는 정보 조회
        """
        student = g.user

        response = {
            'name': student.name,
            'number': student.number,

            'extension_11': {
                'class_num': student.extension_apply_11.class_,
                'seat_num': student.extension_apply_11.seat
            } if student.extension_apply_11 else None,

            'extension_12': {
                'class_num': student.extension_apply_12.class_,
                'seat_num': student.extension_apply_12.seat
            } if student.extension_apply_12 else None,

            'goingout': {
                'sat': student.goingout_apply.on_saturday,
                'sun': student.goingout_apply.on_sunday
            },
            'stay_value': student.stay_apply.value,
            'good_point': student.good_point,
            'bad_point': student.bad_point
        }

        return self.unicode_safe_json_response(response)


@api.resource('/point/history')
class PointHistory(BaseResource):
    @swag_from(POINT_HISTORY_GET)
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
