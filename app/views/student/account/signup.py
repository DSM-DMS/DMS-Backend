from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

# from app.docs.student.account.auth import *
from app.models.account import SignupWaitingModel, StudentModel


class IDVerification(Resource):
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
