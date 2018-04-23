from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.apply.extension import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/student/apply/extension'))


@api.resource('/11')
class Extension11(BaseResource):
    @swag_from(EXTENSION_GET)
    def get(self):
        pass

    @swag_from(EXTENSION_POST)
    def post(self):
        pass

    @swag_from(EXTENSION_DELETE)
    def delete(self):
        pass


@api.resource('/12')
class Extension12(BaseResource):
    @swag_from(EXTENSION_GET)
    def get(self):
        pass

    @swag_from(EXTENSION_POST)
    def post(self):
        pass

    @swag_from(EXTENSION_DELETE)
    def delete(self):
        pass


@api.resource('/11/map')
class Extension11Map(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        pass


@api.resource('/12/map')
class Extension12Map(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        pass