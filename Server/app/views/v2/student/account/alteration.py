from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Blueprint, Response, abort, g, request, current_app
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.alteration import *
from app.models.account import StudentModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/account'


@api.resource('')
class Account(BaseResource):
    @swag_from(ACCOUNT_DELETE)
    def delete(self):
        pass


@api.resource('/change-pw')
class ChangePW(BaseResource):
    @json_required({'currentPassword': str, 'newPassword': str})
    @auth_required(StudentModel)
    @swag_from(CHANGE_PW_POST)
    def post(self):
        """
        학생 비밀번호 변경
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        current_password = request.json['currentPassword']
        new_password = request.json['newPassword']

        encrypted_current_password = self.encrypt(current_password)

        if student.pw != encrypted_current_password:
            abort(403)

        student.update(pw=new_password)
        return Response('', 200)
