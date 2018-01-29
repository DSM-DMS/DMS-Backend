import json

from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort
from flasgger import swag_from

from app.docs.student.account.info import MYPAGE_GET
from app.models.account import StudentModel
from app.views import BaseResource

api = Api(Blueprint('student-info-api', __name__))


@api.resource('/mypage')
class MyPage(BaseResource):
    @swag_from(MYPAGE_GET)
    @jwt_required
    def get(self):
        """
        마이페이지에 해당하는 정보 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            abort(403)

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

        return Response(json.dumps(response, ensure_ascii=False), content_type='application/json; charset=utf8')
