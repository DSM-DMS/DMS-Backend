from datetime import datetime, time

from flask import Blueprint, Response, g, request, current_app
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.apply.goingout import *
from app.models.account import StudentModel
from app.models.apply import GoingoutApplyModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/apply/goingout'


@api.resource('')
class Goingout(BaseResource):
    @swag_from(GOINGOUT_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 외출 정보 확인
        """
        goingout = GoingoutApplyModel.objects(student=g.user).first()

        if not goingout:
            goingout = GoingoutApplyModel(
                student=g.user,
                on_saturday=False,
                on_sunday=False
            )

        return {
            'sat': goingout.on_saturday,
            'sun': goingout.on_sunday
        }

    @swag_from(GOINGOUT_POST)
    @auth_required(StudentModel)
    @json_required({'sat': bool, 'sun': bool})
    def post(self):
        """
        학생 외출 신청
        """
        payload = request.json

        now = datetime.now()

        if current_app.testing or (now.weekday() == 6 and now.time() > time(20, 30)) or (0 <= now.weekday() < 5) or (now.weekday() == 5 and now.time() < time(22, 00)):
            GoingoutApplyModel(student=g.user, on_saturday=payload['sat'], on_sunday=payload['sun']).save()

            return Response('', 201)

        return Response('', 204)
