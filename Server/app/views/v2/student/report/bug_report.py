from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.report.bug_report import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/report'


@api.resource('/bug')
class BugReport(BaseResource):
    @swag_from(BUG_REPORT_POST)
    def post(self):
        pass
