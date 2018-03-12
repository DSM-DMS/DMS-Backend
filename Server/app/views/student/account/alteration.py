from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Blueprint, Response, current_app, g, request
from flask_restful import Api, abort
from flasgger import swag_from

from app.docs.student.account.alteration import *
from app.support.resources import BaseResource
from app.support.view_decorators import student_only

api = Api(Blueprint('student-account-alteration-api', __name__))


@api.resource('/change/pw')
class ChangePW(BaseResource):
    @swag_from(CHANGE_PW_POST)
    @student_only
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

        student = g.user

        if student.pw != current_pw:
            abort(403)

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


@api.resource('/change/number')
class ChangeNumber(BaseResource):
    @swag_from(CHANGE_NUMBER_POST)
    @student_only
    def post(self):
        """
        학번 변경
        """
        new_number = int(request.form['new_number'])

        student = g.user
        student.update(number=new_number)

        return Response('', 200)
