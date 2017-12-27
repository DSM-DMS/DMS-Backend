import openpyxl

from flask import Response, send_from_directory
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from flasgger import swag_from

from app.docs.admin.apply.goingout import *
from app.models.account import AdminModel, StudentModel


class AdminGoingout(Resource):
    @swag_from(GOINGOUT_GET)
    @jwt_required
    def get(self):
        """
        외출신청 엑셀 다운로드
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        wb = openpyxl.load_workbook('외출 명렬표.xlsx')
        ws = wb.active

        for row in map(str, range(3, 68)):
            for column1, column2, column3 in zip(['B', 'F', 'J', 'N'], ['D', 'H', 'L', 'P'], ['E', 'I', 'M', 'Q']):
                if ws[column1+row].value == '학번':
                    continue

                number = int(ws[column1 + row].value or 0)
                student = StudentModel.objects(number=number).first()
                if not (student and student.goingout_apply):
                    continue

                sat = '토요 외출' if student.goingout_apply.on_saturday else ''
                sun = '일요 외출' if student.goingout_apply.on_sunday else ''
                ws[column2+row] = sat
                ws[column3+row] = sun

        wb.save('명렬표.xlsx')

        return send_from_directory('.', '외출 명렬표.xlsx'), 200
