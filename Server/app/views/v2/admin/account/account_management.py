from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Blueprint, Response, abort, current_app, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.account_management import *
from app.models.account import AdminModel, StudentModel, SignupWaitingModel
from app.views.v2 import BaseResource, auth_required, json_required_2

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/account-management'


@api.resource('/student')
class StudentAccount(BaseResource):
    @auth_required(AdminModel)
    @json_required_2({'number': int})
    @swag_from(STUDENT_ACCOUNT_DELETE)
    def delete(self):
        """
        학생 계정 제거
        """
        student_number = request.json['number']

        student = StudentModel.objects(number=student_number).first()

        if not student:
            # 해당 학번에 대해 학생이 존재하지 않는 경우

            signup_waiting = SignupWaitingModel.objects(number=student_number).first()
            # signup waiting에서 한 번 더 조회

            if not signup_waiting:
                return Response('', 204)
                # 여기에도 없다면 204
            else:
                return {
                    'uuid': signup_waiting.uuid
                }
        else:
            # 학생이 존재하는 경우 : 학생 계정을 삭제하며 새로운 UUID를 발급하는 비즈니스 로직을 진행
            new_uuid = str(uuid4())[:4]

            signup_waiting = SignupWaitingModel(
                uuid=new_uuid,
                name=student.name,
                number=student.number
            ).save()

            if signup_waiting:
                # 성공
                student.delete()

                return {
                    'uuid': signup_waiting.uuid
                }, 201
            else:
                raise Exception()


@api.resource('/admin')
class AdminAccount(BaseResource):
    @auth_required(AdminModel)
    @json_required_2({'id': str, 'password': str, 'name': str})
    @swag_from(ADMIN_ACCOUNT_POST)
    def post(self):
        """
        새로운 관리자 계정 생성
        """
        id = request.json['id']
        password = request.json['password']
        name = request.json['name']

        if AdminModel.objects(id=id).first():
            abort(409)

        encrypted_password = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')

        admin = AdminModel(
            id=id,
            pw=encrypted_password,
            name=name
        ).save()

        if admin:
            return Response('', 201)
        else:
            raise Exception()

    @auth_required(AdminModel)
    @json_required_2({'id': str})
    @swag_from(ADMIN_ACCOUNT_DELETE)
    def delete(self):
        """
        관리자 계정 제거
        """
        id = request.json['id']

        admin = AdminModel.objects(id=id).first()

        if not admin:
            return Response('', 204)
        else:
            admin.delete()

            return Response('', 200)
