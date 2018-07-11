from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.auth import *
from app.models.account import StudentModel
from app.models.token import AccessTokenModelV2, RefreshTokenModelV2
from app.views.v2 import BaseResource, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student'


@api.resource('/auth')
class Auth(BaseResource):
    @json_required({'id': str, 'password': str})
    @swag_from(AUTH_POST)
    def post(self):
        """
        학생 로그인 
        """
        payload = request.json

        student = StudentModel.objects(id=payload['id'], pw=self.encrypt_password(payload['password'])).first()

        return ({
            'accessToken': AccessTokenModelV2.create_access_token(student, request.headers['USER-AGENT']),
            'refreshToken': RefreshTokenModelV2.create_refresh_token(student, request.headers['USER-AGENT'])
        }, 201) if student else Response('', 401)
