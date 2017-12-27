from datetime import datetime, time

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.apply.stay import *
from app.models.account import StudentModel
from app.models.apply import StayApplyModel


class Stay(Resource):
    @swag_from(STAY_GET)
    @jwt_required
    def get(self):
        """
        잔류신청 정보 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        return {
            'value': student.stay_apply.value
        }, 200

    @swag_from(STAY_POST)
    @jwt_required
    def post(self):
        """
        잔류신청
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        now = datetime.now()

        if (now.weekday() == 6 and now.time() > time(20, 30)) or (0 < now.weekday() < 3) or (now.weekday() == 3 and now.time() < time(22, 00)):
            # 신청 가능 범위
            # - 일요일 오후 8시 30분 이후부터 목요일 오후 10시까지
            # weekday는 월요일이 0, 일요일이 6
            value = int(request.form['value'])

            student.update(stay_apply=StayApplyModel(value=value))

            return Response('', 201)
        else:
            return Response('', 204)
