from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.auth import *
from app.models.account import AdminModel
from app.models.token import AccessTokenModelV2, RefreshTokenModelV2
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

        admin = AdminModel.objects(id=payload['id'], pw=self.encrypt_password(payload['password'])).first()

        user_agent = request.headers.get('USER-AGENT', 'Windows Application') or 'Windows Application'

        return ({
            'accessToken': AccessTokenModelV2.create_access_token(admin, user_agent),
            'refreshToken': RefreshTokenModelV2.create_refresh_token(admin, user_agent)
        }, 201) if admin else Response('', 401)
