from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Api
from flasgger import swag_from

from app.docs.admin.report.facility_report import *
from app.models.report import FacilityReportModel
from app.views import BaseResource

api = Api(Blueprint('admin-facility-report-api', __name__))
api.prefix = '/admin'


@api.resource('/report/facility')
class FacilityReportDownload(BaseResource):
    @swag_from(FACILITY_REPORT_DOWNLOAD_GET)
    @jwt_required
    @BaseResource.admin_only
    def get(self):
        """
        시설고장신고 리스트 조회
        """
        response = [{
            'author': facility_report.author,
            'title': facility_report.title,
            'content': facility_report.content,
            'room': facility_report.room
        } for facility_report in FacilityReportModel.objects]

        return self.unicode_safe_json_response(response)
