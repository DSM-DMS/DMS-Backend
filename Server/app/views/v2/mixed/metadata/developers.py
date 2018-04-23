from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.metadata.developers import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/metadata'))


@api.resource('/developer-info')
class DeveloperInfo(BaseResource):
    @swag_from(DEVELOPER_INFO_GET)
    def get(self):
        pass
