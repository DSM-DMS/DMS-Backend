from flask import Blueprint, Response, request
from flask_restful import Api



from app.models.version import VersionModel
from app.views.v1 import BaseResource
from app.views.v1 import admin_only


api = Api(Blueprint('version-check-api', __name__))


@api.resource('/version')
class Version(BaseResource):
    def __init__(self):
        self.PLATFORM_TYPES = {
            'web': 1,
            'android': 2,
            'ios': 3
        }
        
        super(Version, self).__init__()

    
    def get(self):
        """
        플랫폼의 최신 버전 확인 
        """
        platform = self.PLATFORM_TYPES[request.args['platform']]

        newest = VersionModel.objects(platform=platform).first()
        if newest:
            return self.unicode_safe_json_response({'newest_version': newest.version})
        else:
            return Response('', 204)

    
    @admin_only
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
