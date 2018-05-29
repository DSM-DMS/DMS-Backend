from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Blueprint, abort, current_app, request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.account.auth import *
from app.models.account import AdminModel, RefreshTokenModel
from app.views.v2 import BaseResource, json_required_2

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin'


@api.resource('/auth')
class Auth(BaseResource):
    @json_required_2({'id': str, 'password': str})
    @swag_from(AUTH_POST)
    def post(self):
        """
        관리자 로그인
        """
        id = request.json['id']
        password = request.json['password']

        encrypted_password = self.encrypt_password(password)

        admin = AdminModel.objects(id=id, pw=encrypted_password).first()

        if not admin:
            abort(401)
        else:
            refresh_token = uuid4()

            RefreshTokenModel(
                token=refresh_token,
                token_owner=admin,
                pw_snapshot=encrypted_password
            ).save()

            return {
                'accessToken': create_access_token(id),
                'refreshToken': create_refresh_token(str(refresh_token))
            }, 201
