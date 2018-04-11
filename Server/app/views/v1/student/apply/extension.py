from datetime import datetime

from flask import Blueprint, Response, current_app, g, request
from flask_restful import Api
from flasgger import swag_from

from app.views.v1 import BaseResource
from app.views.v1 import student_only

from app.docs.v1.student.apply.extension import *
from app.models.v2.apply import ExtensionApply11Model, ExtensionApply12Model

from utils.extension_meta import APPLY_START, APPLY_END_11, APPLY_END_12, MAPS

api = Api(Blueprint('student-extension-api', __name__))


@api.resource('/extension/11')
class Extension11(BaseResource):
    @swag_from(EXTENSION_GET)
    @student_only
    def get(self):
        """
        11시 연장신청 정보 조회
        """
        student = g.user

        apply = ExtensionApply11Model.objects(student=student)

        return ({
            'class_num': apply.class_,
            'seat_num': apply.seat
        }, 200) if apply else ('', 204)

    @swag_from(EXTENSION_POST)
    @student_only
    def post(self):
        """
        11시 연장신청
        """
        student = g.user

        now = datetime.now().time()

        if not current_app.testing and not APPLY_START < now < APPLY_END_11:
            # Not testing, can't apply
            return Response('', 204)

        class_ = int(request.form['class_num'])
        seat = int(request.form['seat_num'])

        apply = ExtensionApply11Model.objects(student=student).first()
        if apply:
            apply.delete()

        ExtensionApply11Model(student=student, class_=class_, seat=seat, apply_date=datetime.now()).save()

        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    @student_only
    def delete(self):
        """
        11시 연장신청 취소
        """
        student = g.user

        now = datetime.now().time()

        if not current_app.testing and not APPLY_START < now < APPLY_END_11:
            # Not testing, can't apply
            return Response('', 204)

        ExtensionApply11Model.objects(student=student).delete()

        return Response('', 200)


@api.resource('/extension/12')
class Extension12(BaseResource):
    @swag_from(EXTENSION_GET)
    @student_only
    def get(self):
        """
        12시 연장신청 정보 조회
        """
        student = g.user

        apply = ExtensionApply12Model.objects(student=student)

        return ({
            'class_num': apply.class_,
            'seat_num': apply.seat
        }, 200) if apply else ('', 204)

    @swag_from(EXTENSION_POST)
    @student_only
    def post(self):
        """
        12시 연장신청
        """
        student = g.user

        now = datetime.now().time()

        if not current_app.testing and not APPLY_START < now < APPLY_END_12:
            # Not testing, can't apply
            return Response('', 204)

        class_ = int(request.form['class_num'])
        seat = int(request.form['seat_num'])

        apply = ExtensionApply12Model.objects(student=student).first()
        if apply:
            apply.delete()

        ExtensionApply12Model(student=student, class_=class_, seat=seat, apply_date=datetime.now()).save()

        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    @student_only
    def delete(self):
        """
        12시 연장신청 취소
        """
        student = g.user

        now = datetime.now().time()

        if not current_app.testing and not APPLY_START < now < APPLY_END_12:
            # Not testing, can't apply
            return Response('', 204)

        ExtensionApply12Model.objects(student=student).delete()

        return Response('', 200)


def _create_extension_map(class_, hour):
    seat_count = 1

    map_ = MAPS[class_]
    for i, row in enumerate(map_):
        for j, seat in enumerate(row):
            if map_[i][j]:
                apply = ExtensionApply11Model.objects(class_=class_, seat=seat_count).first() if hour == 11 \
                    else ExtensionApply12Model.objects(class_=class_, seat=seat_count).first()

                if apply:
                    map_[i][j] = apply.student.name
                else:
                    map_[i][j] = seat_count

                seat_count += 1

    return map_


@api.resource('/extension/map/11')
class ExtensionMap11(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        """
        11시 연장신청 지도 조회
        """
        class_ = int(request.args['class_num'])

        return self.unicode_safe_json_response(_create_extension_map(class_, 11))


@api.resource('/extension/map/12')
class ExtensionMap12(BaseResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        """
        12시 연장신청 지도 조회
        """
        class_ = int(request.args['class_num'])

        return self.unicode_safe_json_response(_create_extension_map(class_, 12))
