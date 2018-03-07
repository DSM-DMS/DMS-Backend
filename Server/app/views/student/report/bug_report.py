from datetime import datetime
import os
from slacker import Slacker

from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.student.report.bug_report import *
from app.models.account import StudentModel
from app.models.report import BugReportModel
from app.views import BaseResource

api = Api(Blueprint('student-bug-report-api', __name__))


@api.resource('/report/bug')
class BugReport(BaseResource):
    @swag_from(BUG_REPORT_POST)
    @BaseResource.student_only
    def post(self):
        """
        버그 신고
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        title = request.form['title']
        content = request.form['content']
        time = datetime.now()

        report = BugReportModel(author=student.name, title=title, content=content, report_time=time).save()

        slack_token = os.getenv('SLACK_BOT_TOKEN')
        slack_bot = Slacker(slack_token)
        slack_bot.chat.post_message(channel='#bug-report', text='제보자: {0}\n제보시간: {1}\n제목: {2}\n내용: {3}'.format(student.name, time, title, content))

        return self.unicode_safe_json_response({
            'id': str(report.id)
        }, 201)
