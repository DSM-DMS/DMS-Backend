from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.report.facility import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/report'


@api.resource('/facility')
class FacilityReport(BaseResource):
    @swag_from(FACILITY_REPORT_GET)
    def get(self):
        """
        시설고장신고 조회
        """


@api.resource('/facility/<id>')
class FacilityReportAlteration(BaseResource):
    @swag_from(FACILITY_REPORT_DELETE)
    def delete(self, id):
        """
        시설고장신고 삭제
        """
