from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Blueprint, Response, current_app
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.student.account.signup import *
from app.models.account import SignupWaitingModel, StudentModel, AdminModel
from app.views import BaseResource

api = Api(Blueprint('student-signup-api', __name__))


@api.resource('/verify/id')
class IDVerification(BaseResource):
    @swag_from(ID_VERIFICATION_POST)
    def post(self):
        """
        ID 중복체크
        """
        id = request.form['id']

        student = StudentModel.objects(id=id).first()
        admin = AdminModel.objects(id=id).first()
        if any((student, admin)):
            # ID already exists
            return Response('', 204)
        else:
            return Response('', 200)


@api.resource('/verify/uuid')
class UUIDVerification(BaseResource):
    @swag_from(UUID_VERIFICATION_POST)
    def post(self):
        """
        UUID에 대한 가입 가능 여부 검사
        """
        uuid = request.form['uuid']

        signup_waiting = SignupWaitingModel.objects(uuid=uuid)
        if signup_waiting:
            # Signup available
            return Response('', 200)
        else:
            return Response('', 204)


@api.resource('/signup')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        """
        회원가입
        API 내부에서 한 번 더 ID 중복체크와 UUID 가입 가능 여부를 검사함
        """
        uuid = request.form['uuid']
        id = request.form['id']
        pw = request.form['pw']

        signup_waiting = SignupWaitingModel.objects(uuid=uuid).first()
        student = StudentModel.objects(id=id).first()
        # To validate

        if not signup_waiting:
            # Signup unavailable
            return Response('', 205)

        if student:
            # Already signed
            return Response('', 204)

        # --- Create new student account_admin

        name = signup_waiting.name
        number = signup_waiting.number

        signup_waiting.delete()

        pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        StudentModel(
            id=id,
            pw=pw,
            name=name,
            number=number,
            good_point=0,
            bad_point=0,
            penalty_training_status=0
        )
        StudentModel(id=id, pw=pw, name=name, number=number).save()

        return Response('', 201)
