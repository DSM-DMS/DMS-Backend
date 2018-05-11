from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.post.preview import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/post-preview'


@api.resource('/<category>')
class Preview(BaseResource):
    @swag_from(PREVIEW_POST)
    def post(self):
        pass
