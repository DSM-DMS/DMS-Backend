from uuid import uuid4

from flask import Response, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource, request
from flasgger import swag_from

# 여긴 문서의 경로가 들어갈 것이다.
from app.models.account import SignupWaitingModel, StudentModel, AdminModel


class AccountControl(Resource):
    @jwt_required
    def delete(self):
        """
        학생 계정 삭제
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        number = request.form['number']
        student = StudentModel.objects(
            number=number
        ).first()

        if not student:
            return Response('', 204)

        name = student.name
        student.delete()

        uuid = uuid4()
        SignupWaitingModel(
            uuid=str(uuid),
            name=name,
            number=number
        ).save()

        return Response('', 200)

    @jwt_required
    def get(self):
        """
        StudentWatingModel uuid 확인
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        number = request.form['number']
        sign_up = SignupWaitingModel.objects(
            number=number
        ).first()

        if sign_up:
            return {'uuid': sign_up.uuid}, 200
        else:
            return Response('', 204)
