from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.etc.version import *
from app.models.version import VersionModel
from app.support.resources import BaseResource


api = Api(Blueprint('version-check-api', __name__))


@api.resource('/version')
class Version(BaseResource):
    @swag_from(VERSION_GET)
    def get(self):
        """
        플랫폼의 최신 버전 확인 
        """
        platform = request.args['platform']

        newest = VersionModel.objects(platform=platform).first().version
        if newest:
            return self.unicode_safe_json_response({'newest_version': newest})
        else:
            return Response('', 204)

    @swag_from(VERSION_POST)
    @BaseResource.admin_only
    def post(self):
        """
        플랫폼의 최신 버전 등록
        """
        platform = request.form['platform']
        version = request.form['version']

        past = VersionModel.objects(platform=platform).first()

        if past:
            past.delete()

        VersionModel(
            platform=platform,
            version=version
        ).save()
        return Response('', 201)
