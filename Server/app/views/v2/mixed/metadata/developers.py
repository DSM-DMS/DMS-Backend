from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.metadata.developers import *
from app.views.v2 import BaseResource

api = Api(Blueprint(__name__, __name__))
api.prefix = '/metadata'


@api.resource('/developer-info')
class DeveloperInfo(BaseResource):
    @swag_from(DEVELOPER_INFO_GET)
    def get(self):
        """
        개발자 정보 조회
        """
        return self.unicode_safe_json_dumps({
            'app': ['조성빈', '이병찬', '윤정현', '이성현'],
            'server': ['김성래', '조민규', '인상민'],
            'webFrontend': ['김지수', '김건', '서윤호', '김형규', '오인서', '윤효상'],
            'desktop': ['김경식', '정원태', '김동현', '이종현', '류근찬'],
            'design': ['윤여환', '김동규']
        })
