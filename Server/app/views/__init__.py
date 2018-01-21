from flask_restful import Api

from app.views.admin.account.auth import *
from app.views.admin.account.account_control import *
from app.views.admin.account.signup import *
from app.views.admin.apply.extension import *
from app.views.admin.apply.goingout import *
from app.views.admin.apply.stay import *
from app.views.admin.point.point import *
from app.views.admin.point.rule import *
from app.views.admin.point.student import *
from app.views.admin.post.faq import *
from app.views.admin.post.notice import *
from app.views.admin.post.preview import *
from app.views.admin.post.rule import *
from app.views.admin.report.bug_report import *
from app.views.admin.report.facility_report import *
from app.views.admin.survey.survey import *
from app.views.mixed.post.faq import *
from app.views.mixed.post.notice import *
from app.views.mixed.post.preview import *
from app.views.mixed.post.rule import *
from app.views.mixed.school_data.meal import *
from app.views.student.account.alteration import *
from app.views.student.account.auth import *
from app.views.student.account.info import *
from app.views.student.account.signup import *
from app.views.student.apply.extension import *
from app.views.student.apply.goingout import *
from app.views.student.apply.stay import *
from app.views.student.report.bug_report import *
from app.views.student.report.facility_report import *
from app.views.student.survey.survey import *


class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        # Admin account_admin
        api.add_resource(AdminAuth, '/admin/auth')
        api.add_resource(AdminRefresh, '/admin/refresh')
        api.add_resource(AccountControl, '/admin/account-control')
        api.add_resource(NewAccount, '/admin/new-account')

        api.add_resource(Extension11Download, '/admin/extension/11')
        api.add_resource(Extension12Download, '/admin/extension/12')
        api.add_resource(GoingoutDownload, '/admin/goingout')
        api.add_resource(StayDownload, '/admin/stay')

        api.add_resource(StudentManaging, '/admin/managing/student')
        api.add_resource(PointRuleManaging, '/admin/managing/rule')
        api.add_resource(PointManaging, '/admin/managing/point')

        api.add_resource(FAQPreviewManaging, '/admin/preview/faq')
        api.add_resource(NoticePreviewManaging, '/admin/preview/notice')
        api.add_resource(RulePreviewManaging, '/admin/preview/rule')

        api.add_resource(FAQManaging, '/admin/faq')
        api.add_resource(NoticeManaging, '/admin/notice')
        api.add_resource(RuleManaging, '/admin/rule')

        api.add_resource(BugReportDownload, '/admin/report/bug')
        api.add_resource(FacilityReportDownload, '/admin/report/facility')

        api.add_resource(SurveyManaging, '/admin/survey')
        api.add_resource(QuestionManaging, '/admin/survey/question')

        # Student account_admin
        api.add_resource(ChangePW, '/change/pw')
        api.add_resource(ChangeNumber, '/change/number')
        api.add_resource(Auth, '/auth')
        api.add_resource(AuthCheck, '/auth-check')
        api.add_resource(Refresh, '/refresh')
        api.add_resource(MyPage, '/mypage')
        api.add_resource(IDVerification, '/verify/id')
        api.add_resource(UUIDVerification, '/verify/uuid')
        api.add_resource(Signup, '/signup')

        # Student apply
        api.add_resource(Extension11, '/extension/11')
        api.add_resource(Extension12, '/extension/12')
        api.add_resource(ExtensionMap11, '/extension/map/11')
        api.add_resource(ExtensionMap12, '/extension/map/12')
        api.add_resource(Goingout, '/goingout')
        api.add_resource(Stay, '/stay')

        from app.views.mixed.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app.views.mixed.school_data import meal
        app.register_blueprint(meal.api.blueprint)

        api.add_resource(BugReport, '/report/bug')
        api.add_resource(FacilityReport, '/report/facility')

        # Mixed school_data
        api.add_resource(Survey, '/survey')
        api.add_resource(Question, '/survey/question')
