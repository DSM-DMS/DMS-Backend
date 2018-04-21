from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.student import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/point/student', __name__, url_prefix='/admin/point'))


@api.resource('/student')
class Student(BaseResource):
    @swag_from(STUDENT_GET)
    def get(self):
        pass


@api.resource('/student/penalty')
class StudentPenalty(BaseResource):
    @swag_from(STUDENT_PENALTY_PATCH)
    def patch(self):
        pass
