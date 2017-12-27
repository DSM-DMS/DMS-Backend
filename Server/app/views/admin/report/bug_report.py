import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.account import AdminModel
from app.models.report import BugReportModel


class AdminBugReport(Resource):
    @jwt_required
    def get(self):
        """
        버그신고 리스트 조회
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        return Response(
            json.dumps(
                [{
                    'author': bug_report.author.name,
                    'title': bug_report.title,
                    'content': bug_report.content
                } for bug_report in BugReportModel.objects],
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )
