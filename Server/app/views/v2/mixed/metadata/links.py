from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.metadata.links import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/metadata'))


@api.resource('/links')
class Links(BaseResource):
    @swag_from(LINKS_GET)
    def get(self):
        pass
