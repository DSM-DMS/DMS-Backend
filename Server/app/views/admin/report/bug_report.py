from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.views import BaseResource
from app.views import admin_only

from app.docs.admin.report.bug_report import *
from app.models.report import BugReportModel
from app.models.support.mongo_helper import mongo_to_dict

api = Api(Blueprint('admin-bug-report-api', __name__))
api.prefix = '/admin'


@api.resource('/report/bug')
class BugReportDownload(BaseResource):
    @swag_from(BUG_REPORT_DOWNLOAD_GET)
    @admin_only
    def get(self):
        """
        버그신고 리스트 조회
        """
        response = [mongo_to_dict(report, ['id', 'report_time']) for report in BugReportModel.objects]

        return self.unicode_safe_json_response(response)
