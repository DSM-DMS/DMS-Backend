from flask_restful import Api

from app.views.admin.account.auth import *
from app.views.admin.account.account_control import *
from app.views.admin.account.signup import *
from app.views.admin.apply.afterschool import *
from app.views.admin.apply.extension import *
from app.views.admin.apply.goingout import *
from app.views.admin.apply.stay import *
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
        api.add_resource(AccountControl, '/account_control')
        api.add_resource(AdminRefresh, '/admin/refresh')

        api.add_resource(AdminNewAccount, '/admin/new-account_admin')
        api.add_resource(AdminExtension11, '/admin/extension/11')
        api.add_resource(AdminExtension12, '/admin/extension/12')
        api.add_resource(AdminGoingout, '/admin/goingout')
        api.add_resource(AdminStay, '/admin/stay')

        api.add_resource(AdminFAQPreview, '/admin/preview/faq')
        api.add_resource(AdminNoticePreview, '/admin/preview/notice')
        api.add_resource(AdminRulePreview, '/admin/preview/rule')

        api.add_resource(AdminFAQ, '/admin/faq')
        api.add_resource(AdminNotice, '/admin/notice')
        api.add_resource(AdminRule, '/admin/rule')

        api.add_resource(AdminBugReport, '/admin/report/bug')
        api.add_resource(AdminFacilityReport, '/admin/report/facility')

        api.add_resource(AdminSurvey, '/admin/survey')
        api.add_resource(AdminQuestion, '/admin/survey/question')

        # Student account_admin
        api.add_resource(ChangePW, '/change/pw')
        api.add_resource(ChangeNumber, '/change/number')
        api.add_resource(Auth, '/auth')
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

        # Mixed post
        api.add_resource(FAQPreview, '/preview/faq')
        api.add_resource(NoticePreview, '/preview/notice')
        api.add_resource(RulePreview, '/preview/rule')

        api.add_resource(FAQList, '/faq')
        api.add_resource(FAQItem, '/faq/<post_id>')
        api.add_resource(NoticeList, '/notice')
        api.add_resource(NoticeItem, '/notice/<post_id>')
        api.add_resource(RuleList, '/rule')
        api.add_resource(RuleItem, '/rule/<post_id>')

        api.add_resource(BugReport, '/report/bug')
        api.add_resource(FacilityReport, '/report/facility')

        # Mixed school_data
        api.add_resource(Meal, '/meal/<date>')
        api.add_resource(Survey, '/survey')
        api.add_resource(Question, '/survey/question')
