from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.report.facility_report import *
from app.models.account import StudentModel
from app.models.report import FacilityReportModel
from app.views.v2 import BaseResource, auth_required, json_required_2

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/report'


@api.resource('/facility')
class FacilityReport(BaseResource):
    @swag_from(FACILITY_REPORT_POST)
    @auth_required(StudentModel)
    @json_required_2({'content': str, 'room': int})
    def post(self):
        """
        시설 고장 신고 
        """
        student = g.user
        room = request.json['room']
        content = request.json['content']

        report = FacilityReportModel(
            author=student.name,
            room=room,
            content=content
        ).save()

        return self.unicode_safe_json_dumps({
            'id': str(report.id)
        }, 201)