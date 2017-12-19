from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Response, current_app
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.account.signup import *
from app.models.account import SignupWaitingModel, StudentModel


class IDVerification(Resource):
    @swag_from(ID_VERIFICATION_POST)
    def post(self):
        """
        ID 중복체크
        """
        id = request.form['id']

        student = StudentModel.objects(
            id=id
        ).first()

        if student:
            # ID already exists
            return Response('', 204)
        else:
            return Response('', 200)


class UUIDVerification(Resource):
    @swag_from(UUID_VERIFICATION_POST)
    def post(self):
        """
        UUID에 대한 가입 가능 여부 검사
        """
        uuid = request.form['uuid']

        signup_waiting = SignupWaitingModel.objects(
            uuid=uuid
        )

        if signup_waiting:
            # Signup available
            return Response('', 200)
        else:
            return Response('', 204)


class Signup(Resource):
    @swag_from(SIGNUP_POST)
    def post(self):
        """
        회원가입
        API 내부에서 한 번 더 ID 중복체크와 UUID 가입 가능 여부를 검사함
        """
        uuid = request.form['uuid']
        id = request.form['id']
        pw = request.form['pw']

        signup_waiting = SignupWaitingModel.objects(
            uuid=uuid
        )

        student = StudentModel.objects(
            id=id
        ).first()

        if not signup_waiting:
            # Signup unavailable
            return Response('', 205)

        if student:
            # Already signed
            return Response('', 204)

        # --- Create new student account

        name = signup_waiting.name
        number = signup_waiting.number

        signup_waiting.delete()

        pw = hexlify(
            data=pbkdf2_hmac(
                hash_name='sha256',
                password=pw.encode(),
                salt=current_app.secret_key.encode(),
                iterations=100000
            )
        ).decode('utf-8')

        StudentModel(
            id=id,
            pw=pw,
            name=name,
            number=number
        ).save()

        return Response('', 201)
