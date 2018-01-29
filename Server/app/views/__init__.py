from flask_restful import Api

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


class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        from app.views.admin.account import account_control, auth, signup
        app.register_blueprint(account_control.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

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

        from app.views.admin.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app.views.admin.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app.views.student.account import alteration, auth, info, signup
        app.register_blueprint(alteration.api.blueprint)
        app.register_blueprint(auth.api.blueprint)
        app.register_blueprint(info.api.blueprint)
        app.register_blueprint(signup.api.blueprint)

        from app.views.student.apply import extension, goingout, stay
        app.register_blueprint(extension.api.blueprint)
        app.register_blueprint(goingout.api.blueprint)
        app.register_blueprint(stay.api.blueprint)

        from app.views.student.report import bug_report, facility_report
        app.register_blueprint(bug_report.api.blueprint)
        app.register_blueprint(facility_report.api.blueprint)

        from app.views.student.survey import survey
        app.register_blueprint(survey.api.blueprint)

        from app.views.mixed.post import faq, notice, preview, rule
        app.register_blueprint(faq.api.blueprint)
        app.register_blueprint(notice.api.blueprint)
        app.register_blueprint(preview.api.blueprint)
        app.register_blueprint(rule.api.blueprint)

        from app.views.mixed.school_data import meal
        app.register_blueprint(meal.api.blueprint)

