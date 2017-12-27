from uuid import uuid4

from flask import Response
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
        학생 계정 제거 후 새로운 UUID 생성
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        number = request.form['number']
        student = StudentModel.objects(number=number).first()

        if not student:
            return Response('', 204)

        name = student.name
        student.delete()

        SignupWaitingModel(
            uuid=str(uuid4()),
            name=name,
            number=number
        ).save()

        return Response('', 200)

    @jwt_required
    def get(self):
        """
        특정 학번에 해당하는 UUID 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        number = request.form['number']
        signup_waiting = SignupWaitingModel.objects(number=number).first()

        if signup_waiting:
            return {
                'uuid': signup_waiting.uuid
            }, 200
        else:
            return Response('', 204)
