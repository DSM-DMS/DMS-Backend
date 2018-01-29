from uuid import uuid4

from flask import Blueprint, Response
from flask_restful import Api, request
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from app.docs.admin.account.account_control import *
from app.models.account import SignupWaitingModel, StudentModel
from app.views import BaseResource

api = Api(Blueprint('admin-account-control-api', __name__))
api.prefix = '/admin'


@api.resource('/account-control')
class AccountControl(BaseResource):
    @swag_from(ACCOUNT_CONTROL_POST)
    @jwt_required
    @BaseResource.admin_only
    def post(self):
        """
        학생 계정 제거 후 새로운 UUID 생성
        """
        number = int(request.form['number'])
        student = StudentModel.objects(number=number).first()

        if student:
            name = student.name
            student.delete()

            while True:
                uuid = str(uuid4())[:4]

                if not SignupWaitingModel.objects(uuid=str(uuid)):
                    SignupWaitingModel(
                        uuid=uuid,
                        name=name,
                        number=number
                    ).save()

                    break

        signup_waiting = SignupWaitingModel.objects(number=number).first()

        if not signup_waiting:
            return Response('', 204)

        uuid = signup_waiting.uuid

        return self.unicode_safe_json_response({
            'uuid': uuid
        }, 201)
