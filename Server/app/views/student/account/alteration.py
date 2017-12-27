from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.account.alteration import *
from app.models.account import StudentModel


class ChangePW(Resource):
    @swag_from(CHANGE_PW_POST)
    @jwt_required
    def post(self):
        """
        비밀번호 변경
        """
        current_pw = request.form['current_pw']

        current_pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=current_pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode()
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        student = StudentModel.objects(id=get_jwt_identity(), pw=current_pw).first()
        # Validate account

        if not student:
            return Response('', 403)

        # --- Change password

        new_pw = request.form['new_pw']
        new_pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=new_pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode()
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        student.update(pw=new_pw)

        return Response('', 200)


class ChangeNumber(Resource):
    @swag_from(CHANGE_NUMBER_POST)
    @jwt_required
    def post(self):
        """
        학번 변경
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        new_number = int(request.form['new_number'])

        student.update(number=new_number)

        return Response('', 200)
