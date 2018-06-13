from flask import Blueprint, g
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.account.info import *
from app.models.account import StudentModel
from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel
from app.views.v2 import BaseResource, auth_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/info'


@api.resource('/apply')
class ApplyInfo(BaseResource):
    @swag_from(APPLY_INFO_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 신청 정보 확인
        """
        extension11 = ExtensionApply11Model.objects(student=g.user).first()
        extension12 = ExtensionApply12Model.objects(student=g.user).first()
        goingout = GoingoutApplyModel.objects(student=g.user).first()
        stay = StayApplyModel.objects(student=g.user).first()

        return {
            'extension11': {
                'classNum': extension11.class_,
                'seatNum': extension11.seat
            } if extension11 else None,
            'extension12': {
                'classNum': extension12.class_,
                'seatNum': extension12.seat
            } if extension12 else None,
            'goingout': {
                'sat': goingout.on_saturday,
                'sun': goingout.on_sunday
            },
            'stay': stay.value
        }


@api.resource('/mypage')
class MyPage(BaseResource):
    @swag_from(MYPAGE_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 마이페이지 정보 조회
        """
        return self.unicode_safe_json_dumps({
            'badPoint': g.user.bad_point,
            'goodPoint': g.user.good_point,
            'name': g.user.name,
            'number': g.user.number
        })


@api.resource('/point-history')
class PointHistory(BaseResource):
    @swag_from(POINT_HISTORY_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        상벌점 내역 조회
        """
        return self.unicode_safe_json_dumps([
            {
                'point': history.point,
                'pointType': history.point_type,
                'reason': history.reason,
                'time': history.time.strftime('%Y-%m-%d')
            } for history in g.user.point_histories
        ])
