from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.excel.extension import *
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/extension'))


@api.resource('/11')
class Extension11ExcelDownload(BaseResource):
    @swag_from(EXTENSION_11_EXCEL_DOWNLOAD_GET)
    def get(self):
        pass


@api.resource('/12')
class Extension12ExcelDownload(BaseResource):
    @swag_from(EXTENSION_12_EXCEL_DOWNLOAD_GET)
    def get(self):
        pass
