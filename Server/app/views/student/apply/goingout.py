from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.student.apply.goingout import *
from app.models.account import StudentModel
from app.models.apply import GoingoutApplyModel
from app.views import BaseResource

api = Api(Blueprint('student-goingout-api', __name__))


@api.resource('/goingout')
class Goingout(BaseResource):
    @swag_from(GOINGOUT_GET)
    @jwt_required
    @BaseResource.student_only
    def get(self):
        """
        외출신청 정보 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        return self.unicode_safe_json_response({
            'sat': student.goingout_apply.on_saturday,
            'sun': student.goingout_apply.on_sunday
        }, 200)

    @swag_from(GOINGOUT_POST)
    @jwt_required
    @BaseResource.student_only
    def post(self):
        """
        외출신청
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        sat = request.form['sat'].upper() == 'TRUE'
        sun = request.form['sun'].upper() == 'TRUE'

        student.update(goingout_apply=GoingoutApplyModel(on_saturday=sat,on_sunday=sun))

        return Response('', 201)
