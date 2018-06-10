from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.signup import *
from app.models.account import StudentModel, SignupWaitingModel
from app.views.v2 import BaseResource, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student'


@api.resource('/verify/id')
class IDVerification(BaseResource):
    """
    학생 ID 중복체크
    """
    @swag_from(ID_VERIFICATION_POST)
    @json_required({'id': str})
    def post(self):
        id = request.json['id']

        student = StudentModel.objects(id=id).first()
        if student:
            abort(409)
        else:
            return Response('', 200)


@api.resource('/verify/uuid')
class UUIDVerification(BaseResource):
    """
    학생 UUID 검증
    """
    @swag_from(UUID_VERIFICATION_POST)
    @json_required({'uuid': str})
    def post(self):
        uuid = request.json['uuid']

        signup_waiting = SignupWaitingModel(uuid=uuid).first()
        if signup_waiting:
            return Response('', 200)
        else:
            return Response('', 204)


@api.resource('/signup')
class Signup(BaseResource):
    """
    학생 회원가입
    """
    @swag_from(SIGNUP_POST)
    @json_required({'uuid': str, 'id': str, 'password': str})
    def post(self):
        uuid = request.json['uuid']
        id = request.json['id']
        password = request.json['password']

        student = StudentModel.objects(id=id).first()
        if student:
            return Response('', 204)

        signup_waiting = SignupWaitingModel.objects(uuid=uuid).first()
        if not signup_waiting:
            return Response('', 205)

        encrypted_password = self.encrypt_password(password)

        StudentModel(
            id=id,
            pw=encrypted_password,
            name=signup_waiting.name,
            number=signup_waiting.number
        ).save()

        signup_waiting.delete()

        return Response('', 201)