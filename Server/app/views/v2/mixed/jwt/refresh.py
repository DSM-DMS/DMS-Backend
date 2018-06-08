from uuid import UUID

from flask import Blueprint, Response, abort, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.jwt.refresh import *
from app.models.account import TokenModel, AccessTokenModel, RefreshTokenModel
from app.views.v2 import BaseResource

api = Api(Blueprint(__name__, __name__))
api.prefix = '/jwt'


@api.resource('/refresh')
class Refresh(BaseResource):
    @jwt_refresh_token_required
    @swag_from(REFRESH_GET)
    def get(self):
        try:
            token = RefreshTokenModel.objects(identity=UUID(get_jwt_identity())).first()

            if not token:
                abort(401)

            if token.owner.pw != token.pw_snapshot:
                return Response('', 205)

            return {
                'accessToken': create_access_token(
                    TokenModel.generate_token(AccessTokenModel, token.owner, request.headers['USER-AGENT']))
            }
        except ValueError:
            abort(401)
