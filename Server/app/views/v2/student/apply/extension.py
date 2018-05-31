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


@api.resource('/11')
class Extension11(BaseResource):
    @swag_from(EXTENSION_GET)
    @auth_required(StudentModel)
    def get(self):
        """
        학생 11시 연장 신청 정보 조회
        """
        student = g.user
        extension = ExtensionApply11Model.objects(student=student).first()

        return self.unicode_safe_json_dumps({
            'classNum': extension.class_,
            'seatNum': extension.seat
        })

    @swag_from(EXTENSION_POST)
    @auth_required(StudentModel)
    @json_required({'classNum': int, 'seatNum': str})
    def post(self):
        """
        학생 11시 연장 신청
        """
        student = g.user

        now = datetime.now().time()

        if not current_app.testing and not APPLY_START < now < APPLY_END_11:
            return Response('', 204)

        class_ = request.json['classNum']
        seat = request.json['seatNum']

        extension = ExtensionApply11Model.objects(student=student).first()
        if extension:
            extension.delete()

        extension = ExtensionApply11Model.objects(class_=class_, seat=seat).first()
        if extension:
            return Response('', 205)

        ExtensionApply11Model(
            class_=class_,
            seat=seat
        ).save()

        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    @auth_required(StudentModel)
    def delete(self):
        """
        학생 11시 연장 신청 취소
        """
        student = g.user

        now = datetime.now().time()

        extension = ExtensionApply11Model.objects(student=student).first()
        if (not current_app.testing and not APPLY_START < now < APPLY_END_11) and (not extension):
            return Response('', 204)

        extension.delete()

        return Response('', 200)


@api.resource('/12')
class Extension12(BaseResource):
    @swag_from(EXTENSION_GET)
    def get(self):
        """
        학생 12시 연장 신청 정보 조회
        """
        student = g.user
        extension = ExtensionApply12Model.objects(student=student).first()

        return self.unicode_safe_json_dumps({
            'classNum': extension.class_,
            'seatNum': extension.seat
        })

    @swag_from(EXTENSION_POST)
    def post(self):
        """
        학생 12시 연장 신청
        """
        student = g.user

        now = datetime.now().time()

        if not current_app.testing and not APPLY_START < now < APPLY_END_12:
            return Response('', 204)

        class_ = request.json['classNum']
        seat = request.json['seatNum']

        extension = ExtensionApply12Model.objects(student=student).first()
        if extension:
            extension.delete()

        extension = ExtensionApply12Model.objects(class_=class_, seat=seat).first()
        if extension:
            return Response('', 205)

        ExtensionApply12Model(
            class_=class_,
            seat=seat
        ).save()

        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    def delete(self):
        """
        학생 12시 연장 신청 취소
        """
        student = g.user

        now = datetime.now().time()

        extension = ExtensionApply12Model.objects(student=student).first()
        if (not current_app.testing and not APPLY_START < now < APPLY_END_12) and (not extension):
            return Response('', 204)

        extension.delete()

        return Response('', 200)


@api.resource('/11/map')
class Extension11Map(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        pass


@api.resource('/12/map')
class Extension12Map(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        pass