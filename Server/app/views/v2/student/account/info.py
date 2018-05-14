from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.info import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/info'


@api.resource('/apply')
class ApplyInfo(BaseResource):
    @swag_from(APPLY_INFO_GET)
    def get(self):
        pass


@api.resource('/mypage')
class MyPage(BaseResource):
    @swag_from(MYPAGE_GET)
    def get(self):
        pass


@api.resource('/point-history')
class PointHistory(BaseResource):
    @swag_from(POINT_HISTORY_GET)
    def get(self):
        pass
