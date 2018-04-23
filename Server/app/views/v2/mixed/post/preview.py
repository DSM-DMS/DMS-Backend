from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.post.preview import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/preview'))


@api.resource('/faq')
class FAQPreview(BaseResource):
    @swag_from(FAQ_PREVIEW_GET)
    def get(self):
        pass


@api.resource('/notice')
class NoticePreview(BaseResource):
    @swag_from(NOTICE_PREVIEW_GET)
    def get(self):
        pass


@api.resource('/rule')
class RulePreview(BaseResource):
    @swag_from(RULE_PREVIEW_GET)
    def get(self):
        pass
