from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.metadata.links import *
from app.views.v2 import BaseResource

api = Api(Blueprint(__name__, __name__))
api.prefix = '/metadata'


@api.resource('/links')
class Links(BaseResource):
    @swag_from(LINKS_GET)
    def get(self):
        """
        DMS 관련 링크 조회
        """
        return {
            'facebook': 'https://www.facebook.com/DMSforDSM/',
            'github': 'https://github.com/DSM-DMS',
            'android': 'https://play.google.com/store/apps/details?id=teamdms.dms_kotlin',
            'ios': 'https://itunes.apple.com/KR/app/id1328234395?mt=8'
        }
