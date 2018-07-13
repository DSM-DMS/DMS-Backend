from datetime import datetime
from slacker import Slacker

from flask import Blueprint, Response, g, request, current_app
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.report.bug_report import *
from app.models.account import StudentModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/report'


@api.resource('/bug')
class BugReport(BaseResource):
    def __init__(self):
        self.slack_bot = Slacker(current_app.config['SLACK_BOT_TOKEN'])

        self.PLATFORM_TYPES = {
            1: 'Web',
            2: 'Android',
            3: 'iOS'
        }

        super(BugReport, self).__init__()

    @swag_from(BUG_REPORT_POST)
    @json_required({'platform': int, 'content': str})
    @auth_required(StudentModel)
    def post(self):
        """
        학생 버그 신고
        """
        payload = request.json

        self.slack_bot.chat.post_message(
            channel='#bug-report{}'.format('-for-test' if current_app.testing else ''),
            text='제보자: {}\n제보시간: {}\n플랫폼: {}\n내용: {}'.format(
                g.user.name,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                self.PLATFORM_TYPES[payload['platform']],
                payload['content']
            )
        )

        return Response('', 201)
