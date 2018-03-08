from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Blueprint, current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api, abort, request

from app.models.account import SystemModel, RefreshTokenModel
from app.views import BaseResource

api = Api(Blueprint('system-auth-api', __name__))
api.prefix = '/system'


@api.resource('/auth')
class Auth(BaseResource):
    def post(self):
        """
        시스템 계정 로그인
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

        system = SystemModel.objects(id=id, pw=pw).first()

        if not system:
            abort(401)

        # --- Auth success

        refresh_token = uuid4()
        RefreshTokenModel(
            token=refresh_token,
            token_owner=system,
            pw_snapshot=pw
        ).save()
        # Generate new refresh token made up of uuid4

        return self.unicode_safe_json_response({
            'access_token': create_access_token(id),
            'refresh_token': create_refresh_token(str(refresh_token))
        }, 200)


@api.resource('/refresh')
class Refresh(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        """
        새로운 Access Token 획득
        """
        token = RefreshTokenModel.objects(token=get_jwt_identity()).first()

        # if not token or token.token_owner.pw != token.pw_snapshot:
        #     # Invalid token or the token issuing password is different from the current password
        #     # Returns status code 205 : Reset Content
        #     return Response('', 205)

        return self.unicode_safe_json_response({
            'access_token': create_access_token(token.token_owner.id)
        }, 200)
