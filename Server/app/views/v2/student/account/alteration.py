from flask import Blueprint, Response, abort, request, g
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.alteration import *
from app.models.account import StudentModel
from app.views.v2 import BaseResource, auth_required, json_required_2

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/account'


@api.resource('/change-pw')
class ChangePW(BaseResource):
    @json_required_2({'currentPassword': str, 'newPassword': str})
    @auth_required(StudentModel)
    @swag_from(CHANGE_PW_POST)
    def post(self):
        """
        학생 비밀번호 변경
        """
        student = g.user

        current_password = request.json['currentPassword']
        new_password = request.json['newPassword']

        encrypted_current_password = self.encrypt_password(current_password)

        if student.pw != encrypted_current_password:
            abort(403)

        encrypted_new_password = self.encrypt_password(new_password)

        student.update(pw=encrypted_new_password)
        return Response('', 200)
