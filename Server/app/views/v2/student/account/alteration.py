from flask import Blueprint, Response, abort, request, g
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.alteration import *
from app.models.account import StudentModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/account'


@api.resource('/change-pw')
class ChangePW(BaseResource):
    @json_required({'currentPassword': str, 'newPassword': str})
    @auth_required(StudentModel)
    @swag_from(CHANGE_PW_POST)
    def post(self):
        """
        학생 비밀번호 변경
        """
        payload = request.json

        if g.user.pw != self.encrypt_password(payload['currentPassword']):
            abort(403)

        g.user.update(pw=self.encrypt_password(payload['newPassword']))

        return Response('', 200)
