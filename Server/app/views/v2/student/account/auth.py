from flask import Blueprint, Response, request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.auth import *
from app.models.account import StudentModel, TokenModel, AccessTokenModel, RefreshTokenModel
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
            'accessToken': create_access_token(TokenModel.generate_token(AccessTokenModel, student, request.headers['USER-AGENT'])),
            'refreshToken': create_refresh_token(TokenModel.generate_token(RefreshTokenModel, student, request.headers['USER-AGENT']))
        }, 201) if student else Response('', 401)
