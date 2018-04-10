from datetime import datetime
from slacker import Slacker

from flask import Blueprint, current_app, g, request
from flask_restful import Api
from flasgger import swag_from

from app_v1.views import BaseResource
from app_v1.views import student_only

from app_v1.docs.student.report.bug_report import *
from app_v2.models.report import BugReportModel

api = Api(Blueprint('student-bug-report-api', __name__))


@api.resource('/report/bug')
class BugReport(BaseResource):
    def __init__(self):
        self.PLATFORM_TYPES = {
            1: 'Web',
            2: 'Android',
            3: 'iOS'
        }

    @swag_from(BUG_REPORT_POST)
    @student_only
    def post(self):
        """
        버그 신고
        """
        student = g.user

        content = request.form['content']
        platform_type = int(request.form['platform_type'])
        time = datetime.now()

        report = BugReportModel(author=student.name, content=content, platform_type=platform_type, report_time=time).save()

        if not current_app.testing:
            slack_bot = Slacker(current_app.config['SLACK_BOT_TOKEN'])
            slack_bot.chat.post_message(channel='#bug-report', text='제보자: {}\n제보시간: {}\n플랫폼: {}\n내용: {}'
                                        .format(student.name, str(time)[:-7], self.PLATFORM_TYPES[platform_type], content))

        return self.unicode_safe_json_response({
            'id': str(report.id)
        }, 201)
