from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.admin.report.facility_report import *
from app.models.report import FacilityReportModel
from app.support.resources import BaseResource
from app.support.view_decorators import admin_only

api = Api(Blueprint('admin-facility-report-api', __name__))
api.prefix = '/admin'


@api.resource('/report/facility')
class FacilityReport(BaseResource):
    @swag_from(FACILITY_REPORT_GET)
    @admin_only
    def get(self):
        """
        시설고장신고 정보 조회
        """
        response = [{
            'id': str(facility_report.id),
            'author': facility_report.author,
            'title': facility_report.title,
            'content': facility_report.content,
            'room': facility_report.room
        } for facility_report in FacilityReportModel.objects]

        return self.unicode_safe_json_response(response)

    @swag_from(FACILITY_REPORT_DELETE)
    @admin_only
    def delete(self):
        """
        시설고장신고 삭제(해결 완료)
        """
        report_id = request.form['report_id']
        if len(report_id) != 24:
            return Response('', 204)

        report = FacilityReportModel.objects(id=report_id).first()
        if not report:
            return Response('', 204)

        report.delete()

        return Response('', 200)
