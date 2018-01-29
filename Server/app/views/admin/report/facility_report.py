import json

from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort
from flasgger import swag_from

from app.docs.admin.report.facility_report import *
from app.models.account import AdminModel
from app.models.report import FacilityReportModel
from app.views import BaseResource

api = Api(Blueprint('admin-facility-report-api', __name__))
api.prefix = '/admin'


@api.resource('/report/facility')
class FacilityReportDownload(BaseResource):
    @swag_from(FACILITY_REPORT_DOWNLOAD_GET)
    @jwt_required
    def get(self):
        """
        시설고장신고 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        response = [{
            'author': facility_report.author,
            'title': facility_report.title,
            'content': facility_report.content,
            'room': facility_report.room
        } for facility_report in FacilityReportModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), content_type='application/json; charset=utf8')
