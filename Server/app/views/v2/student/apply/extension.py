from datetime import datetime

from flask import Blueprint, Response, abort, g, request, current_app
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.student.apply.extension import *
from app.models.account import StudentModel
from app.models.apply import ExtensionApply11Model, ExtensionApply12Model
from app.views.v2 import BaseResource, auth_required, json_required

from utils.extension_meta import APPLY_START, APPLY_END_11, APPLY_END_12, MAPS

api = Api(Blueprint(__name__, __name__))
api.prefix = '/student/apply/extension'


def can_apply(end_time):
    return APPLY_START < datetime.now().time() < end_time


def can_apply_11():
    return can_apply(APPLY_END_11)


def can_apply_12():
    return can_apply(APPLY_END_12)


def apply_extension(model, class_num, seat_num) -> bool:
    if model.objects(class_=class_num, seat=seat_num):
        return False
    else:
        model(
            student=g.user,
            class_=class_num,
            seat=seat_num
        ).save()

        return True


@api.resource('/11')
class Extension11(BaseResource):
    @swag_from(EXTENSION_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 11시 연장 신청 정보 조회
        """
        extension = ExtensionApply11Model.objects(student=g.user).first()

        return self.unicode_safe_json_dumps({
            'classNum': extension.class_,
            'seatNum': extension.seat
        }) if extension else Response('', 204)

    @swag_from(EXTENSION_POST)
    @auth_required(StudentModel)
    @json_required({'classNum': int, 'seatNum': str})
    def post(self):
        """
        학생 11시 연장 신청
        """
        if not(current_app.testing or can_apply_11()):
            return Response('', 204)

        payload = request.json

        return Response('', 201 if apply_extension(ExtensionApply11Model, payload['classNum'], payload['seatNum']) else 205)

    @swag_from(EXTENSION_DELETE)
    @auth_required(StudentModel)
    def delete(self):
        """
        학생 11시 연장 신청 취소
        """
        if not(current_app.testing or can_apply_11()):
            return Response('', 204)

        ExtensionApply11Model.objects(student=g.user).delete()

        return Response('', 200)


@api.resource('/12')
class Extension12(BaseResource):
    @swag_from(EXTENSION_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 12시 연장 신청 정보 조회
        """
        extension = ExtensionApply12Model.objects(student=g.user).first()

        return self.unicode_safe_json_dumps({
            'classNum': extension.class_,
            'seatNum': extension.seat
        }) if extension else Response('', 204)

    @swag_from(EXTENSION_POST)
    @auth_required(StudentModel)
    @json_required({'classNum': int, 'seatNum': str})
    def post(self):
        """
        학생 12시 연장 신청
        """
        if not(current_app.testing or can_apply_12()):
            return Response('', 204)

        payload = request.json

        return Response('', 201 if apply_extension(ExtensionApply12Model, payload['classNum'], payload['seatNum']) else 205)

    @swag_from(EXTENSION_DELETE)
    @auth_required(StudentModel)
    def delete(self):
        """
        학생 12시 연장 신청 취소
        """
        if not(current_app.testing or can_apply_12()):
            return Response('', 204)

        ExtensionApply12Model.objects(student=g.user).delete()

        return Response('', 200)


def _create_extension_map(class_, model):
    seat_count = 1

    map_ = MAPS[class_]
    for i, row in enumerate(map_):
        for j, seat in enumerate(row):
            if map_[i][j]:
                apply = model.objects(class_=class_, seat=seat_count).first()

                if apply:
                    map_[i][j] = apply.student.name
                else:
                    map_[i][j] = seat_count

                seat_count += 1

    return map_


@api.resource('/11/map')
class Extension11Map(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        11시 연장 신청 지도 조회
        """
        try:
            return self.unicode_safe_json_response(_create_extension_map(int(request.args['classNum']), ExtensionApply11Model))
        except ValueError:
            abort(400)


@api.resource('/12/map')
class Extension12Map(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        12시 연장 신청 지도 조회
        """
        try:
            return self.unicode_safe_json_response(_create_extension_map(int(request.args['classNum']), ExtensionApply12Model))
        except ValueError:
            abort(400)
