from datetime import datetime

from flask import Blueprint, g, request
from flask_restful import Api, abort
from flasgger import swag_from

from app.docs.student.report.facility_report import *
from app.models.report import FacilityReportModel
from app.support.resources import BaseResource
from app.support.view_decorators import student_only

api = Api(Blueprint('student-facility-report-api', __name__))


@api.resource('/report/facility')
class FacilityReport(BaseResource):
    @swag_from(FACILITY_REPORT_POST)
    @student_only
    def post(self):
        """
        시설고장 신고
        """
        student = g.user

        title = request.form['title']
        content = request.form['content']
        room = int(request.form['room'])

        if not 200 < room < 519:
            abort(400)

        report = FacilityReportModel(author=student.name, title=title, content=content, room=room, report_time=datetime.now()).save()

        return self.unicode_safe_json_response({
            'id': str(report.id)
        }, 201)
