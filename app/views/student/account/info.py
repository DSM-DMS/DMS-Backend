import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from flasgger import swag_from

from app.docs.student.account.info import MYPAGE_GET
from app.models.account import StudentModel


class MyPage(Resource):
    @swag_from(MYPAGE_GET)
    @jwt_required
    def get(self):
        """
        마이페이지에 해당하는 정보 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        return Response(json.dumps({
            'signup_date': student.signup_date,
            'name': student.name,
            'number': student.number,

            'extension_11': {
                'class': student.extension_apply_11.class_,
                'seat': student.extension_apply_11.seat
            } if student.extension_apply_11 else None,

            'extension_12': {
                'class': student.extension_apply_12.class_,
                'seat': student.extension_apply_12.seat
            } if student.extension_apply_12 else None,

            'goingout': {
                'sat': student.goingout_apply.on_saturday,
                'sun': student.goingout_apply.on_sunday
            },
            'stay_value': student.stay_apply.value
        }, ensure_ascii=False), 200, content_type='application/json; charset=utf8')
