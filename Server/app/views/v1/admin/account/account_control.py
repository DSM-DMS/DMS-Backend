from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Blueprint, Response, request, current_app
from flask_restful import Api


from app.views.v1 import BaseResource
from app.views.v1 import admin_only


from app.models.account import SignupWaitingModel, StudentModel, AdminModel

api = Api(Blueprint('admin-account-control-api', __name__))
api.prefix = '/admin'


@api.resource('/account-control')
class AccountControl(BaseResource):

    @admin_only
    def post(self):
        """
        학생 계정 비밀번호 변경
        """
        number = int(request.form['number'])
        student = StudentModel.objects(number=number).first()
        pw = request.form['pw']

        if not student:
            return Response('', 204)

        pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')

        student.update(pw=pw)

        return Response('', 201)


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

    @admin_only
    def get(self):
        """
        학생 계정 회원가입 상태 확인
        """
        return self.unicode_safe_json_response({
            'unsigned_student_count': SignupWaitingModel.objects.count(),
            'signed_student_count': StudentModel.objects.count()
        }, 200)
