from openpyxl import Workbook

from flask import Blueprint, send_from_directory
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort
from flasgger import swag_from

from app.docs.admin.apply.extension import *
from app.models.account import AdminModel, StudentModel
from app.views import BaseResource

from utils.apply_excel_manager import get_cells, ready_worksheet

EXTENSION_CLASSES = ['가온실', '나온실', '다온실', '라온실', '3층 독서실', '4층 독서실', '5층 열린교실']

api = Api(Blueprint('admin-extension-api', __name__))
api.prefix = '/admin/extension'


@api.resource('/11')
class Extension11Download(BaseResource):
    @swag_from(EXTENSION_DOWNLOAD_GET)
    @jwt_required
    def get(self):
        """
        11시 연장신청 엑셀 다운로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        wb = Workbook()
        ws = wb.active

        ready_worksheet(ws)

        for student in StudentModel.objects:
            number_cell, name_cell, status_cell = get_cells(student)

            ws[number_cell] = student.number
            ws[name_cell] = student.name

            extension_apply = student.extension_apply_11

            if not extension_apply:
                continue

            ws[status_cell] = EXTENSION_CLASSES[extension_apply.class_ - 1]

        wb.save('11.xlsx')
        wb.close()

        return send_from_directory('../', '11.xlsx')


@api.resource('/12')
class Extension12Download(BaseResource):
    @swag_from(EXTENSION_DOWNLOAD_GET)
    @jwt_required
    def get(self):
        """
        12시 연장신청 엑셀 다운로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        wb = Workbook()
        ws = wb.active

        ready_worksheet(ws)

        for student in StudentModel.objects:
            number_cell, name_cell, status_cell = get_cells(student)

            ws[number_cell] = student.number
            ws[name_cell] = student.name

            extension_apply = student.extension_apply_11

            if not extension_apply:
                continue

            ws[status_cell] = EXTENSION_CLASSES[extension_apply.class_ - 1]

        wb.save('12.xlsx')
        wb.close()

        return send_from_directory('../', '12.xlsx')
