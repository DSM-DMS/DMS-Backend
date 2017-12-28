from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.admin.account.signup import NEW_ACCOUNT_POST
from app.models.account import AdminModel


class NewAccount(Resource):
    @swag_from(NEW_ACCOUNT_POST)
    @jwt_required
    def post(self):
        """
        새로운 관리자 계정 생성
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']

        if AdminModel.objects(id=id):
            return Response('', 204)

        # --- Create new admin account_admin

        pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        AdminModel(id=id, pw=pw, name=name).save()

        return Response('', 201)
