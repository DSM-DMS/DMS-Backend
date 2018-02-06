from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.docs.admin.report.bug_report import *
from app.models.report import BugReportModel
from app.views import BaseResource

api = Api(Blueprint('admin-bug-report-api', __name__))
api.prefix = '/admin'


@api.resource('/report/bug')
class BugReportDownload(BaseResource):
    @swag_from(BUG_REPORT_DOWNLOAD_GET)
    @BaseResource.admin_only
    def get(self):
        """
        버그신고 리스트 조회
        """
        response = [{
            'author': bug_report.author,
            'title': bug_report.title,
            'content': bug_report.content
        } for bug_report in BugReportModel.objects]

        return self.unicode_safe_json_response(response)
