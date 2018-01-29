import json

from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort
from flasgger import swag_from

from app.docs.admin.report.bug_report import *
from app.models.account import AdminModel
from app.models.report import BugReportModel
from app.views import BaseResource

api = Api(Blueprint('admin-bug-report-api', __name__))
api.prefix = '/admin'


@api.resource('/report/bug')
class BugReportDownload(BaseResource):
    @swag_from(BUG_REPORT_DOWNLOAD_GET)
    @jwt_required
    def get(self):
        """
        버그신고 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        response = [{
            'author': bug_report.author,
            'title': bug_report.title,
            'content': bug_report.content
        } for bug_report in BugReportModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), content_type='application/json; charset=utf8')
