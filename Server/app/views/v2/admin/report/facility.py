from flask import Blueprint, Response
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.report.facility import *
from app.models.account import AdminModel
from app.models.report import FacilityReportModel
from app.views.v2 import BaseResource, auth_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/report'


@api.resource('/facility')
class FacilityReport(BaseResource):
    @auth_required(AdminModel)
    @swag_from(FACILITY_REPORT_GET)
    def get(self):
        """
        시설고장신고 조회
        """
        return [{
            'id': str(report.id),
            'author': report.author,
            'content': report.content,
            'room': report.room
        } for report in FacilityReportModel.objects]


@api.resource('/facility/<id>')
class FacilityReportAlteration(BaseResource):
    @auth_required(AdminModel)
    @swag_from(FACILITY_REPORT_DELETE)
    def delete(self, id):
        """
        시설고장신고 삭제
        """
        if len(id) != 24:
            return Response('', 204)

        report = FacilityReportModel.objects(id=id).first()

        if not report:
            return Response('', 204)

        report.delete()

        return Response('', 200)
