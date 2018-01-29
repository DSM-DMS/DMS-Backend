import json

from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.admin.point.student import *
from app.models.account import AdminModel, StudentModel
from app.views import BaseResource

api = Api(Blueprint('admin-student-point-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/student')
class StudentManaging(BaseResource):
    @swag_from(STUDENT_MANAGING_GET)
    @jwt_required
    def get(self):
        """
        학생 목록 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        response = [{
            'id': student.id,
            'name': student.name,
            'number': student.number,
            'good_point': student.good_point,
            'bad_point': student.bad_point,
            'penalty_training_status': student.penalty_training_status
        } for student in StudentModel.objects]

        return self.json_response(response)

    @swag_from(STUDENT_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        새로운 학생 상벌점 데이터 등록
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        good_point = int(request.form['good_point'])
        bad_point = int(request.form['bad_point'])
        penalty_training_status = int(request.form['penalty_training_status'])

        student.update(
            good_point=good_point,
            bad_point=bad_point,
            penalty_training_status=penalty_training_status
        )

        return Response('', 201)
