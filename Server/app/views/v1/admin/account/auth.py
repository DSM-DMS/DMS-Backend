from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import UUID

from flask import Blueprint, current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api, abort

from app.views.v1 import BaseResource

from app.models.account import AdminModel
from app.models.token import AccessTokenModelV2, RefreshTokenModelV2

api = Api(Blueprint('admin-auth-api', __name__))
api.prefix = '/admin'


@api.resource('/auth')
class Auth(BaseResource):

    def post(self):
        """
        관리자 로그인
        """
        id = request.form['id']
        pw = request.form['pw']

        pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        admin = AdminModel.objects(id=id, pw=pw).first()

        if not admin:
            abort(401)

        # --- Auth success
        user_agent = request.headers.get('USER-AGENT', 'Windows Application') or 'Windows Application'

        return self.unicode_safe_json_response({
            'access_token': AccessTokenModelV2.create_access_token(admin, user_agent),
            'refresh_token': RefreshTokenModelV2.create_refresh_token(admin, user_agent)
        }, 200)


@api.resource('/refresh')
class Refresh(BaseResource):

    @jwt_refresh_token_required
    def post(self):
        """
        새로운 Access Token 획득
        """
        token = RefreshTokenModelV2.objects(identity=UUID(get_jwt_identity())).first()

        if not token:
            abort(205)

        user_agent = request.headers.get('USER-AGENT', 'Windows Application') or 'Windows Application'

        return self.unicode_safe_json_response({
            'access_token': AccessTokenModelV2.create_access_token(token.owner, user_agent)
        }, 200)
