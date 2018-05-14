from flask import Blueprint, Response, abort, g, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.jwt.checker import *
from app.models.account import AdminModel, StudentModel, SystemModel
from app.views.v2 import BaseResource

api = Api(Blueprint(__name__, __name__))
api.prefix = '/jwt'


@api.resource('/check')
class AuthCheck(BaseResource):
    @jwt_required
    @swag_from(AUTH_CHECK_GET)
    def get(self):
        """
        로그인 여부 체크
        """
        if not any(
            (
                AdminModel.objects(id=get_jwt_identity()),
                StudentModel.objects(id=get_jwt_identity()),
                SystemModel.objects(id=get_jwt_identity())
            )
        ):
            return Response('', 204)

        return Response('', 200)
