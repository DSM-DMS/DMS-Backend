import openpyxl

from flask import Response, send_from_directory
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from flasgger import swag_from

from app.docs.admin.apply.extension import *
from app.models.account import AdminModel, StudentModel


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

        wb = openpyxl.load_workbook('app/views/admin/apply/list.xlsx')
        ws = wb.active

        for row in map(str, range(3, 68)):
            for column1, column2 in zip(['B', 'F', 'J', 'N'], ['D', 'H', 'L', 'P']):
                if ws[column1 + row].value == '학번':
                    continue

                number = int(ws[column1 + row].value or 0)
                student = StudentModel.objects(number=number).first()
                if not student:
                    continue

                class_ = student.extension_apply_11.class_ if student.extension_apply_11 else 0

                if class_ == 0:
                    status = ''
                elif class_ == 1:
                    status = '가온실'
                elif class_ == 2:
                    status = '나온실'
                elif class_ == 3:
                    status = '다온실'
                elif class_ == 4:
                    status = '라온실'
                elif class_ == 5:
                    status = '3층 독서실'
                elif class_ == 6:
                    status = '4층 독서실'
                elif class_ == 7:
                    status = '5층 독서실'

                ws[column2 + row] = status

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

        wb = openpyxl.load_workbook('app/views/admin/apply/list.xlsx')
        ws = wb.active

        for row in map(str, range(3, 68)):
            for column1, column2 in zip(['B', 'F', 'J', 'N'], ['D', 'H', 'L', 'P']):
                if ws[column1 + row].value == '학번':
                    continue

                number = int(ws[column1 + row].value or 0)
                student = StudentModel.objects(number=number).first()
                if not student:
                    continue

                class_ = student.extension_apply_12.class_ if student.extension_apply_12 else 0

                if class_ == 0:
                    status = ''
                elif class_ == 1:
                    status = '가온실'
                elif class_ == 2:
                    status = '나온실'
                elif class_ == 3:
                    status = '다온실'
                elif class_ == 4:
                    status = '라온실'
                elif class_ == 5:
                    status = '3층 독서실'
                elif class_ == 6:
                    status = '4층 독서실'
                elif class_ == 7:
                    status = '5층 독서실'

                ws[column2 + row] = status

        wb.save('12.xlsx')
        wb.close()

        return send_from_directory('../', '12.xlsx')
