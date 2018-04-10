from uuid import uuid4

from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app_v1.views import BaseResource
from app_v1.views import admin_only

from app_v1.docs.admin.account.account_control import *
from app_v2.models.account import SignupWaitingModel, StudentModel, AdminModel

api = Api(Blueprint('admin-account-control-api', __name__))
api.prefix = '/admin'


@api.resource('/account-control')
class AccountControl(BaseResource):
    @swag_from(ACCOUNT_CONTROL_POST)
    @admin_only
    def post(self):
        """
        학생 계정 제거 후 새로운 UUID 생성
        """
        number = int(request.form['number'])
        student = StudentModel.objects(number=number).first()

        if student:
            # Signed student number
            name = student.name
            student.delete()

            while True:
                uuid = str(uuid4())[:4]

                if not SignupWaitingModel.objects(uuid=uuid):
                    SignupWaitingModel(
                        uuid=uuid,
                        name=name,
                        number=number
                    ).save()

                    break

        signup_waiting = SignupWaitingModel.objects(number=number).first()

        if not signup_waiting:
            return Response('', 204)

        uuid = signup_waiting.uuid

        return self.unicode_safe_json_response({
            'uuid': uuid
        }, 201)

    @swag_from(ACCOUNT_CONTROL_DELETE)
    @admin_only
    def delete(self):
        """
        관리자 계정 삭제 
        """
        id = request.form['id']
        admin = AdminModel.objects(id=id).first()

        if not admin:
            return Response('', 204)

        admin.delete()
        return Response('', 200)


@api.resource('/student-sign-status')
class StudentSignStatus(BaseResource):
    @swag_from(STUDENT_SIGN_STATUS_GET)
    @admin_only
    def get(self):
        """
        학생 계정 회원가입 상태 확인
        """
        return self.unicode_safe_json_response({
            'unsigned_student_count': SignupWaitingModel.objects.count(),
            'signed_student_count': StudentModel.objects.count()
        }, 200)
