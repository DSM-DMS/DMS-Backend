from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.account import StudentModel


class ChangePW(Resource):
    @jwt_required
    def post(self):
        """
        비밀번호 변경
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        current_pw = request.form['current_pw']

        current_pw = hexlify(
            data=pbkdf2_hmac(
                hash_name='sha256',
                password=current_pw.encode(),
                salt=current_app.secret_key.encode(),
                iterations=100000
            )
        ).decode()

        student = StudentModel.objects(
            id=get_jwt_identity(),
            pw=current_pw
        ).first()

        if not student:
            return Response('', 403)

        new_pw = request.form['new_pw']

        new_pw = hexlify(
            data=pbkdf2_hmac(
                hash_name='sha256',
                password=new_pw.encode(),
                salt=current_app.secret_key.encode(),
                iterations=100000
            )
        ).decode()

        student.update(pw=new_pw)

        return Response('', 200)


class ChangeNumber(Resource):
    def post(self):
        """
        학번 변경
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        new_number = int(request.form['new_number'])

        student.update(number=new_number)

        return Response('', 200)
