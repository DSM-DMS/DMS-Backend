from flask import Blueprint, Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort, current_app, request
from flasgger import swag_from

from app.views import BaseResource

api = Api(Blueprint('api', __name__))
api.prefix = '/system'


@api.resource('/apply/extension/11')
class Extension11(BaseResource):
    def delete(self):
        """
        11시 연장신청 정보 제거
        """


@api.resource('/apply/extension/11/<number>')
class Extension11EachStudent(BaseResource):
    def post(self, number):
        """
        특정 학생의 11시 연장신청
        """

    def patch(self, number):
        """
        특정 학생의 11시 연장신청 정보 변경
        """

    def delete(self, number):
        """
        특정 학생의 11시 연장신청 정보 제거
        """


@api.resource('/apply/extension/12')
class Extension12(BaseResource):
    def delete(self):
        """
        12시 연장신청 정보 제거
        """


@api.resource('/apply/extension/12/<number>')
class Extension12EachStudent(BaseResource):
    def post(self, number):
        """
        특정 학생의 12시 연장신청
        """

    def patch(self, number):
        """
        특정 학생의 12시 연장신청 정보 변경
        """

    def delete(self, number):
        """
        특정 학생의 12시 연장신청 정보 제거
        """


@api.resource('/apply/goingout')
class Goingout(BaseResource):
    def delete(self):
        """
        모든 학생의 외출신청 정보 초기화
        """


@api.resource('/apply/goingout/<number>')
class GoingoutEachStudent(BaseResource):
    def delete(self, number):
        """
        특정 학생의 외출신청 정보 제거
        """
