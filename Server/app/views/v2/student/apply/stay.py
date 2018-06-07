from datetime import datetime, time

from flask import Blueprint, Response, abort, g, request, current_app
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.apply.stay import *
from app.models.account import StudentModel
from app.models.apply import StayApplyModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/apply/stay'


@api.resource('')
class Stay(BaseResource):
    @swag_from(STAY_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 잔류 신청 확인
        """
        student = g.user

        stay = StayApplyModel.objects(student=student).first()

        return self.unicode_safe_json_dumps({
            'value': stay.value or None
        })

    @swag_from(STAY_POST)
    @auth_required(StudentModel)
    @json_required({'value': int})
    def post(self):
        """
        학생 잔류 신청
        """
        student = g.user
        now = datetime.now()
        if current_app.testing or (now.weekday() == 6 and now.time() > time(20, 30)) or (0 <= now.weekday() < 3) or (now.weekday() == 3 and now.time() < time(23, 00)):
            # 신청 가능 범위
            # - 일요일 오후 8시 30분 이후부터 목요일 오후 10시까지
            value = request.json['value']

            StayApplyModel.objects(student=student).delete()
            StayApplyModel(student=student, value=value).save()

            return Response('', 201)
        else:
            return Response('', 204)
