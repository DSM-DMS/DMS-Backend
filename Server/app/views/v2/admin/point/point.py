from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.point import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/point/point', __name__, url_prefix='/admin'))


@api.resource('/point')
class Point(BaseResource):
    @swag_from(POINT_GET)
    def get(self):
        pass

    @swag_from(POINT_POST)
    def post(self):
        pass

    @swag_from(POINT_DELETE)
    def patch(self):
        pass
