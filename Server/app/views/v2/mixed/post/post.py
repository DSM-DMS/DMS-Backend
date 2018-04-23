from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.post.faq import *
from app.docs.v2.mixed.post.notice import *
from app.docs.v2.mixed.post.rule import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('mixed/post/post', __name__, url_prefix=''))


@api.resource('/faq')
class FAQList(BaseResource):
    @swag_from(FAQ_LIST_GET)
    def get(self):
        pass


@api.resource('/faq/<post_id>')
class FAQItem(BaseResource):
    @swag_from(FAQ_ITEM_GET)
    def get(self, post_id):
        pass


@api.resource('/notice')
class NoticeList(BaseResource):
    @swag_from(NOTICE_LIST_GET)
    def get(self):
        pass


@api.resource('/notice/<post_id>')
class NoticeItem(BaseResource):
    @swag_from(NOTICE_ITEM_GET)
    def get(self, post_id):
        pass


@api.resource('/rule')
class RuleList(BaseResource):
    @swag_from(RULE_LIST_GET)
    def get(self):
        pass


@api.resource('/rule/<post_id>')
class RuleItem(BaseResource):
    @swag_from(RULE_ITEM_GET)
    def get(self, post_id):
        pass
