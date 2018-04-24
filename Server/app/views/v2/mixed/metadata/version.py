from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.metadata.version import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/metadata'))


@api.resource('/version')
class Version(BaseResource):
    @swag_from(VERSION_GET)
    def get(self):
        pass

    @swag_from(VERSION_POST)
    def post(self):
        pass
