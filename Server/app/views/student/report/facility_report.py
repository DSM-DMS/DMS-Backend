from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, Resource, abort, request
from flasgger import swag_from

from app.docs.student.report.facility_report import *
from app.models.account import StudentModel
from app.models.report import FacilityReportModel

api = Api(Blueprint('student-facility-report-api', __name__))


@api.resource('/report/facility')
class FacilityReport(Resource):
    @swag_from(FACILITY_REPORT_POST)
    @jwt_required
    def post(self):
        """
        시설고장 신고
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            abort(403)

        title = request.form['title']
        content = request.form['content']
        room = int(request.form['room'])

        if not 200 < room < 519:
            return Response('', 400)

        report = FacilityReportModel(author=student.name, title=title, content=content, room=room).save()

        return {
            'id': str(report.id)
        }, 201
