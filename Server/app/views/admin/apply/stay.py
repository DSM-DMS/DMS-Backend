import openpyxl

from flask import Response, send_from_directory
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from flasgger import swag_from

from app.docs.admin.apply.stay import *
from app.models.account import AdminModel, StudentModel


class AdminStay(Resource):
    @swag_from(STAY_GET)
    @jwt_required
    def get(self):
        """
        잔류신청 엑셀 다운로드
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()
        if not admin:
            return Response('', 403)

        wb = openpyxl.load_workbook('잔류 명렬표.xlsx')
        ws = wb.active

        for row in map(str, range(3, 68)):
            for column1, column2 in zip(['B', 'F', 'J', 'N'], ['D', 'H', 'L', 'P']):
                if ws[column1+row].value == '학번':
                    continue

                number = int(ws[column1 + row].value or 0)
                student = StudentModel.objects(number=number).first()
                value = student.stay_apply.value or 0

                if value == 0:
                    status = 0
                elif value == 1:
                    status = '금요 귀가'
                elif value == 2:
                    status = '토요 귀가'
                elif value == 3:
                    status = '토요 귀사'
                elif value == 4:
                    status = '잔류'
                ws[column2+row] = status

        wb.save('명렬표.xlsx')

        return send_from_directory('.', '잔류 명렬표.xlsx'), 200
