from datetime import datetime

from flask import Blueprint, Response, request
from flask_restful import Api, abort

from app.views.v1 import BaseResource
from app.views.v1 import system_only

from app.models.v2.account import StudentModel
from app.models.v2.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel

api = Api(Blueprint('api', __name__))
api.prefix = '/system'


@api.resource('/apply/extension/11')
class Extension11(BaseResource):
    @system_only
    def delete(self):
        """
        11시 연장신청 정보 제거
        """
        ExtensionApply11Model.objects.delete()

        return Response('', 200)


@api.resource('/apply/extension/11/<int:number>')
class Extension11EachStudent(BaseResource):
    @system_only
    def post(self, number):
        """
        특정 학생의 11시 연장신청
        """
        if not request.is_json:
            abort(400)

        student = StudentModel.objects(number=number).first()

        if not student:
            return Response('', 204)

        class_ = request.json['class_num']
        seat = request.json['seat']

        ExtensionApply11Model(student=student, class_=class_, seat=seat, apply_date=datetime.now()).save()

        return Response('', 201)

    @system_only
    def delete(self, number):
        """
        특정 학생의 11시 연장신청 정보 제거
        """
        student = StudentModel.objects(number=number).first()

        if not student:
            return Response('', 204)

        ExtensionApply11Model.objects(student=student).delete()

        return Response('', 200)


@api.resource('/apply/extension/12')
class Extension12(BaseResource):
    @system_only
    def delete(self):
        """
        12시 연장신청 정보 제거
        """
        ExtensionApply12Model.objects.delete()

        return Response('', 200)


@api.resource('/apply/extension/12/<int:number>')
class Extension12EachStudent(BaseResource):
    @system_only
    def post(self, number):
        """
        특정 학생의 12시 연장신청
        """
        if not request.is_json:
            abort(400)

        student = StudentModel.objects(number=number).first()

        if not student:
            return Response('', 204)

        class_ = request.json['class_num']
        seat = request.json['seat']

        ExtensionApply12Model(student=student, class_=class_, seat=seat, apply_date=datetime.now()).save()

        return Response('', 201)

    @system_only
    def delete(self, number):
        """
        특정 학생의 12시 연장신청 정보 제거
        """
        student = StudentModel.objects(number=number).first()

        if not student:
            return Response('', 204)

        ExtensionApply12Model.objects(student=student).delete()

        return Response('', 200)


@api.resource('/apply/goingout')
class Goingout(BaseResource):
    @system_only
    def delete(self):
        """
        모든 학생의 외출신청 정보 초기화
        """
        for student in StudentModel.objects:
            student.update(goingout_apply=GoingoutApplyModel(apply_date=datetime.now()))

        return Response('', 200)
