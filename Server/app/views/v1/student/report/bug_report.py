from datetime import datetime
from slacker import Slacker

from flask import Blueprint, Response, current_app, g, request
from flask_restful import Api
from flasgger import swag_from

from app.views.v1 import BaseResource
from app.views.v1 import student_only

from app.docs.v1.student.report.bug_report import *

api = Api(Blueprint('student-bug-report-api', __name__))


@api.resource('/report/bug')
class BugReport(BaseResource):
    def __init__(self):
        self.PLATFORM_TYPES = {
            1: 'Web',
            2: 'Android',
            3: 'iOS'
        }
        
        super(BugReport, self).__init__()

    @swag_from(BUG_REPORT_POST)
    @student_only
    def post(self):
        """
        버그 신고
        """
        student = g.user

        content = request.form['content']
        try:
            platform_type = int(request.form['platform_type'])
        except:
            platform_type = 1
        time = datetime.now()

        if not current_app.testing:
            slack_bot = Slacker(current_app.config['SLACK_BOT_TOKEN'])
            slack_bot.chat.post_message(channel='#bug-report', text='제보자: {}\n제보시간: {}\n플랫폼: {}\n내용: {}'
                                        .format(student.name, str(time)[:-7], self.PLATFORM_TYPES[platform_type], content))

        return Response('', 201)
