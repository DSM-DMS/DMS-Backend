from datetime import datetime, time

from flask import Blueprint, Response, current_app, g, request
from flask_restful import Api
from flasgger import swag_from

from app.views.v1 import BaseResource
from app.views.v1 import student_only

from app.docs.v1.student.apply.goingout import *
from app.models.apply import GoingoutApplyModel

api = Api(Blueprint('student-goingout-api', __name__))


@api.resource('/goingout')
class Goingout(BaseResource):
    @swag_from(GOINGOUT_GET)
    @student_only
    def get(self):
        """
        외출신청 정보 조회
        """
        student = g.user

        apply = GoingoutApplyModel.objects(student=student).first()

        return self.unicode_safe_json_response({
            'sat': apply.on_saturday,
            'sun': apply.on_sunday
        }, 200)

    @swag_from(GOINGOUT_POST)
    @student_only
    def post(self):
        """
        외출신청
        """
        student = g.user

        now = datetime.now()

        if current_app.testing or (now.weekday() == 6 and now.time() > time(20, 30)) or (0 <= now.weekday() < 4) or (now.weekday() == 4 and now.time() < time(22, 00)):
            sat = request.form['sat'].upper() == 'TRUE'
            sun = request.form['sun'].upper() == 'TRUE'

            GoingoutApplyModel.objects(student=student).first().delete()
            GoingoutApplyModel(student=student, on_saturday=sat, on_sunday=sun, apply_date=datetime.now()).save()

            return Response('', 201)
        else:
            return Response('', 204)
