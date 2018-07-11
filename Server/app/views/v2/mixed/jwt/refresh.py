from uuid import UUID

from flask import Blueprint, Response, abort, request
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.jwt.refresh import *
from app.models.account import RefreshTokenModel
from app.models.token import AccessTokenModelV2, RefreshTokenModelV2
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
                token = RefreshTokenModelV2.objects(identity=UUID(get_jwt_identity())).first()
                if not token:
                    abort(401)

            return {
                'accessToken': AccessTokenModelV2.create_access_token(token.owner if isinstance(token, RefreshTokenModel) else token.key.owner, request.headers['USER-AGENT'])
            } if token.owner.pw == token.pw_snapshot else Response('', 205)
        except ValueError:
            abort(422)
