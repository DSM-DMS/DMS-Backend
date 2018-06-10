from uuid import uuid4

from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.account_management import *
from app.models.account import AdminModel, StudentModel, SignupWaitingModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/account-management'


@api.resource('/student')
class StudentAccount(BaseResource):
    @auth_required(AdminModel)
    @json_required({'number': int})
    @swag_from(STUDENT_ACCOUNT_DELETE)
    def delete(self):
        """
        학생 계정 제거
        """
        def generate_new_signup_waiting_student_account():
            while True:
                new_uuid = str(uuid4())[:4]

                if not SignupWaitingModel.objects(uuid=new_uuid):
                    break

            SignupWaitingModel(uuid=new_uuid, name=student.name, number=student.number).save()

            return new_uuid

        payload = request.json

        student_number = payload['number']

        student = StudentModel.objects(number=student_number).first()

        if not student:
            signup_waiting = SignupWaitingModel.objects(number=student_number).first()

            return {
                'uuid': signup_waiting.uuid
            } if signup_waiting else Response('', 204)
        else:
            student.delete()

            return {
                'uuid': generate_new_signup_waiting_student_account()
            }, 201


@api.resource('/admin')
class AdminAccount(BaseResource):
    @auth_required(AdminModel)
    @json_required({'id': str, 'password': str, 'name': str})
    @swag_from(ADMIN_ACCOUNT_POST)
    def post(self):
        """
        새로운 관리자 계정 생성
        """
        payload = request.json

        id = payload['id']
        password = payload['password']
        name = payload['name']

        if AdminModel.objects(id=id):
            abort(409)

        AdminModel(id=id, pw=self.encrypt_password(password), name=name).save()

        return Response('', 201)

    @auth_required(AdminModel)
    @json_required({'id': str})
    @swag_from(ADMIN_ACCOUNT_DELETE)
    def delete(self):
        """
        관리자 계정 제거
        """
        payload = request.json

        id = payload['id']

        admin = AdminModel.objects(id=id).first()

        if not admin:
            return Response('', 204)
        else:
            admin.delete()

            return Response('', 200)
