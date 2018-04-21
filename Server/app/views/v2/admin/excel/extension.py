from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.excel.extension import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint('/admin/excel/extension', __name__, url_prefix='/admin'))


@api.resource('/extension')
class ExtensionExcelDownload(BaseResource):
    @swag_from(EXTENSION_EXCEL_DOWNLOAD_GET)
    def get(self):
        pass
