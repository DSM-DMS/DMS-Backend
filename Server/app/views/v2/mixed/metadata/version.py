from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.metadata.version import *
from app.models.account import AdminModel
from app.models.version import VersionModel
from app.views.v2 import BaseResource, auth_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/metadata'


@api.resource('/version/<int:platform>')
class Version(BaseResource):
    @swag_from(VERSION_GET)
    def get(self, platform):
        """
        플랫폼에 해당하는 버전 체크
        """
        version = VersionModel.objects(platform=platform).first()

        return {
            'version': version.version
        } if version else Response('', 204)

    @auth_required(AdminModel)
    @swag_from(VERSION_PUT)
    def put(self, platform):
        """
        새로운 버전 업로드
        """
        payload = request.json

        if not 1 <= platform <= 3:
            abort(400)

        VersionModel(platform=platform, version=payload['version']).save()

        return Response('', 200)
