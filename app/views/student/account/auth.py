from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Response, current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.account.auth import *
from app.models.account import StudentModel, RefreshTokenModel


class Auth(Resource):
    @swag_from(AUTH_POST)
    def post(self):
        """
        학생 로그인
        """
        id = request.form['id']
        pw = request.form['pw']

        encrypted_pw = hexlify(
            data=pbkdf2_hmac(
                hash_name='sha256',
                password=pw.encode(),
                salt=current_app.secret_key.encode(),
                iterations=100000
            )
        ).decode('utf-8')

        student = StudentModel.objects(
            id=id,
            pw=encrypted_pw
        ).first()

        if student:
            return Response('', 401)

        refresh_token = uuid4()
        RefreshTokenModel(
            token=refresh_token,
            token_owner=student,
            pw_snapshot=encrypted_pw
        ).save()

        return {
            'access_token': create_access_token(id),
            'refresh_token': create_refresh_token(str(refresh_token))
        }, 200


class Refresh(Resource):
    @swag_from(REFRESH_POST)
    @jwt_refresh_token_required
    def post(self):
        token = RefreshTokenModel.objects(
            token=get_jwt_identity()
        ).first()

        if not token or token.token_owner.pw != token.pw_snapshot:
            return Response('', 205)

        return {
            'access_token': create_access_token(token.token_owner.id)
        }, 200
