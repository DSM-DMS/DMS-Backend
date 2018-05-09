from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.student import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/point/student'))


@api.resource('')
class StudentList(BaseResource):
    @swag_from(STUDENT_LIST_GET)
    def get(self):
        pass


@api.resource('/penalty')
class StudentPenalty(BaseResource):
    @swag_from(STUDENT_PENALTY_PATCH)
    def patch(self):
        pass
