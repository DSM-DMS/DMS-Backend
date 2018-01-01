from openpyxl import Workbook

from flask import Response, send_from_directory
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from flasgger import swag_from

from app.docs.admin.apply.extension import *
from app.models.account import AdminModel, StudentModel
from utils.apply_excel_manager import get_cells

EXTENSION_CLASSES = ['가온실', '나온실', '다온실', '라온실', '3층 독서실', '4층 독서실', '5층 열린교실']


class Extension11Download(Resource):
    @swag_from(EXTENSION_DOWNLOAD_GET)
    @jwt_required
    def get(self):
        """
        11시 연장신청 엑셀 다운로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        wb = Workbook()
        ws = wb.active

        ws['B2'] = ws['F2'] = ws['J2'] = ws['N2'] = ws['B25'] = ws['F25'] = ws['J25'] = ws['N25'] = ws['B47'] = ws['F47'] = ws['J47'] = ws['N47'] = '학번'
        ws['C2'] = ws['G2'] = ws['K2'] = ws['O2'] = ws['C25'] = ws['G25'] = ws['K25'] = ws['O25'] = ws['C47'] = ws['G47'] = ws['K47'] = ws['O47'] = '이름'

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


class Extension12Download(Resource):
    @swag_from(EXTENSION_DOWNLOAD_GET)
    @jwt_required
    def get(self):
        """
        12시 연장신청 엑셀 다운로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        wb = Workbook()
        ws = wb.active

        ws['B2'] = ws['F2'] = ws['J2'] = ws['N2'] = ws['B25'] = ws['F25'] = ws['J25'] = ws['N25'] = ws['B47'] = ws['F47'] = ws['J47'] = ws['N47'] = '학번'
        ws['C2'] = ws['G2'] = ws['K2'] = ws['O2'] = ws['C25'] = ws['G25'] = ws['K25'] = ws['O25'] = ws['C47'] = ws['G47'] = ws['K47'] = ws['O47'] = '이름'

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
