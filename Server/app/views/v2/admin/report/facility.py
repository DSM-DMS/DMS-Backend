from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.report.facility import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/report/facility', __name__, url_prefix='/admin/report'))


@api.resource('/facility')
class FacilityReport(BaseResource):
    @swag_from(FACILITY_REPORT_GET)
    def get(self):
        pass
