from datetime import datetime
import json

from flask import Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.apply.extension import *
from app.models.account import StudentModel
from app.models.apply import ExtensionApplyModel

from utils.extension_meta import *


class Extension11(Resource):
    @swag_from(EXTENSION_GET)
    @jwt_required
    def get(self):
        """
        11시 연장신청 정보 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        return ({
            'class_num': student.extension_apply_11.class_,
            'seat_num': student.extension_apply_11.seat
        }, 200) if student.extension_apply_11 else ('', 204)

    @swag_from(EXTENSION_POST)
    @jwt_required
    def post(self):
        """
        11시 연장신청
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        now = datetime.now().time()

        if not current_app.config['TEST'] and not APPLY_START < now < APPLY_END_11:
            # Not testing, can't apply
            return Response('', 204)

        class_ = int(request.form['class_num'])
        seat = int(request.form['seat_num'])

        student.update(extension_apply_11=ExtensionApplyModel(class_=class_, seat=seat))

        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    @jwt_required
    def delete(self):
        """
        11시 연장신청 취소
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        student.update(extension_apply_11=None)

        return Response('', 200)


class Extension12(Resource):
    @swag_from(EXTENSION_GET)
    @jwt_required
    def get(self):
        """
        12시 연장신청 정보 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        return ({
            'class_num': student.extension_apply_12.class_,
            'seat_num': student.extension_apply_12.seat
        }, 200) if student.extension_apply_12 else ('', 204)

    @swag_from(EXTENSION_POST)
    @jwt_required
    def post(self):
        """
        12시 연장신청
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        now = datetime.now().time()

        if not current_app.config['TEST'] and not APPLY_START < now < APPLY_END_12:
            # Not testing, can't apply
            return Response('', 204)

        class_ = int(request.form['class_num'])
        seat = int(request.form['seat_num'])

        student.update(extension_apply_12=ExtensionApplyModel(class_=class_,seat=seat))

        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    @jwt_required
    def delete(self):
        """
        12시 연장신청 취소
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()
        if not student:
            return Response('', 403)

        student.update(extension_apply_12=None)

        return Response('', 200)


def create_extension_map(class_, hour):
    """
    Creates extension map including applied student names

    :param class_: class number which to create the map
    :type class_: int
    :param hour: 11/12
    :type hour: int

    :return: Generated extension map
    :rtype: list
    """
    map_ = MAPS[class_]

    assert hour == 11 or hour == 12

    if hour == 11:
        applied_students = {student.extension_apply_11.seat: student.name for student in StudentModel.objects() if
                            student.extension_apply_11 and student.extension_apply_11.class_ == class_}
    elif hour == 12:
        applied_students = {student.extension_apply_12.seat: student.name for student in StudentModel.objects() if
                            student.extension_apply_12 and student.extension_apply_12.class_ == class_}
    # Dictionary comprehension generates 'seat: name' pair

    seat_count = 1

    for i, row in enumerate(map_):
        for j, seat in enumerate(row):
            if map_[i][j]:
                if seat_count in applied_students:
                    map_[i][j] = applied_students[seat_count]
                else:
                    map_[i][j] = seat_count

                seat_count += 1

    return map_


class ExtensionMap11(Resource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        """
        11시 연장신청 지도 조회
        """
        class_ = int(request.args['class_num'])

        return Response(json.dumps(create_extension_map(class_, 11), ensure_ascii=False), 200, content_type='application/json; charset=utf8')


class ExtensionMap12(Resource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self):
        """
        12시 연장신청 지도 조회
        """
        class_ = int(request.args['class_num'])

        return Response(json.dumps(create_extension_map(class_, 12), ensure_ascii=False), 200, content_type='application/json; charset=utf8')
