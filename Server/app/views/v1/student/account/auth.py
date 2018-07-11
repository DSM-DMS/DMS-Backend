from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import UUID

from flask import Blueprint, Response, current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api, abort

from app.views.v1 import BaseResource
from app.views.v1 import student_only

from app.models.account import StudentModel
from app.models.token import AccessTokenModelV2, RefreshTokenModelV2

api = Api(Blueprint('student-auth-api', __name__))


@api.resource('/auth')
class Auth(BaseResource):

    def post(self):
        """
        학생 로그인
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

        student = StudentModel.objects(id=id, pw=pw).first()

        if not student:
            abort(401)

        # --- Auth success

        return self.unicode_safe_json_response({
            'accessToken': AccessTokenModelV2.create_access_token(student, request.headers['USER-AGENT']),
            'refreshToken': RefreshTokenModelV2.create_refresh_token(student, request.headers['USER-AGENT'])
        }, 200)


@api.resource('/auth-check')
class AuthCheck(BaseResource):
    @student_only
    def get(self):
        return Response('', 200)


@api.resource('/refresh')
class Refresh(BaseResource):
    
    @jwt_refresh_token_required
    def post(self):
        """
        새로운 Access Token 획득
        """
        try:
            token = RefreshTokenModelV2.objects(identity=UUID(get_jwt_identity())).first()

            if not token:
                # Invalid token or the token issuing password is different from the current password
                # Returns status code 205 : Reset Content
                return Response('', 205)

            return self.unicode_safe_json_response({
                'access_token': AccessTokenModelV2.create_access_token(token.key.owner, request.headers['USER-AGENT'])
            }, 200)
        except ValueError:
            abort(422)
