from flask import Blueprint, Response, abort, g, request
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
        student = g.user
        extension11 = ExtensionApply11Model(student=student).first()
        extension12 = ExtensionApply12Model(student=student).first()

        goingout = GoingoutApplyModel(student=student).first()
        stay = StayApplyModel.objects(student=student).first()

        return self.unicode_safe_json_dumps({
            "extension11": {
                "class": extension11.class_,
                "seat": extension11.seat
            } if extension11 else None,
            "extension12": {
                "class": extension12.class_,
                "seat": extension12.seat
            } if extension12 else None,
            "goingout": {
                "sat": goingout.on_saturday,
                "sun": goingout.on_sunday
            } if goingout else None,
            "stay": stay.value if stay else None
        })


@api.resource('/mypage')
class MyPage(BaseResource):
    @swag_from(MYPAGE_GET)
    @auth_required(StudentModel)
    def get(self):
        student = g.user

        return self.unicode_safe_json_dumps({
            "badPoint": student.bad_point,
            "goodPoint": student.good_point,
            "name": student.name,
            "number": student.number
        })


@api.resource('/point-history')
class PointHistory(BaseResource):
    @swag_from(POINT_HISTORY_GET)
    @auth_required(StudentModel)
    def get(self):
        student = g.user

        return self.unicode_safe_json_dumps([
            {
                "point":history.point,
                "pointType": history.point_type,
                "reason": history.reason,
                "time": history.time
            } for history in student.point_histroies
        ])

