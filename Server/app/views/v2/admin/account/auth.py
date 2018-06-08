from flask import Blueprint, abort, request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.auth import *
from app.models.account import AdminModel, TokenModel, AccessTokenModel, RefreshTokenModel
from app.views.v2 import BaseResource, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin'


@api.resource('/auth')
class Auth(BaseResource):
    @json_required({'id': str, 'password': str})
    @swag_from(AUTH_POST)
    def post(self):
        """
        관리자 로그인
        """
        payload = request.json

        id = payload['id']
        password = payload['password']

        admin = AdminModel.objects(id=id, pw=self.encrypt_password(password)).first()

        if not admin:
            abort(401)
        else:
            return {
                'accessToken': create_access_token(TokenModel.generate_token(AccessTokenModel, admin, request.headers['USER-AGENT'])),
                'refreshToken': create_refresh_token(TokenModel.generate_token(RefreshTokenModel, admin, request.headers['USER-AGENT']))
            }, 201
