from flask_restful import Api

from app.views.student.account.alteration import *
from app.views.student.account.auth import *
from app.views.student.account.info import *
from app.views.student.account.signup import *
from app.views.student.apply.extension import *
from app.views.student.apply.goingout import *
from app.views.student.apply.stay import *


class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        api.add_resource(ChangePW, '/change/pw')
        api.add_resource(ChangeNumber, '/change/number')
        api.add_resource(Auth, '/auth')
        api.add_resource(Refresh, '/refresh')
        api.add_resource(MyPage, '/mypage')
        api.add_resource(IDVerification, '/verify/id')
        api.add_resource(UUIDVerification, '/verify/uuid')
        api.add_resource(Signup, '/signup')

        api.add_resource(Extension11, '/extension/11')
        api.add_resource(Extension12, '/extension/12')
        api.add_resource(ExtensionMap11, '/extension/map/11')
        api.add_resource(ExtensionMap12, '/extension/map/12')
        api.add_resource(Goingout, '/goingout')
        api.add_resource(Stay, '/stay')
