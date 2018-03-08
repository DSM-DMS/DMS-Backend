from openpyxl import Workbook

from flask import Blueprint, send_from_directory
from flask_restful import Api
from flasgger import swag_from

from app.docs.admin.apply.goingout import *
from app.models.account import StudentModel
from app.views import BaseResource

from utils.excel_style_manager import get_cell_positions_from_student_number, ready_applyment_worksheet

api = Api(Blueprint('admin-goingout-api', __name__))
api.prefix = '/admin'


@api.resource('/goingout')
class GoingoutDownload(BaseResource):
    @swag_from(GOINGOUT_DOWNLOAD_GET)
    @BaseResource.admin_only
    def get(self):
        """
        외출신청 엑셀 다운로드
        """
        wb = Workbook()
        ws = wb.active

        ready_applyment_worksheet(ws)

        for student in StudentModel.objects:
            number_cell, name_cell, status_cell = get_cell_positions_from_student_number(student)
            print('이새끼 엑셀 준비 중임 : {}'.format(student.name))
            print('근데 그 전에 셀에 있던 데이터 이거임 : {}, {}'.format(ws[number_cell].value, ws[name_cell].value))

            if student.stay_apply.value < 3:
                print('{} 이새끼 외출 무시'.format(student.name))
                continue

            number_cell, name_cell, status_cell = get_cell_positions_from_student_number(student)

            print('{} 이새끼 외출 인정'.format(student.name))

            ws[number_cell] = student.number
            ws[name_cell] = student.name

            goingout_apply = student.goingout_apply

            if goingout_apply.on_saturday and goingout_apply.on_sunday:
                status = '토요일, 일요일 외출'
            elif goingout_apply.on_saturday:
                status = '토요일 외출'
            elif goingout_apply.on_sunday:
                status = '일요일 외출'
            else:
                status = ''
            ws.column_dimensions['D'].width = 20
            ws.column_dimensions['H'].width = 20
            ws.column_dimensions['L'].width = 20
            ws.column_dimensions['P'].width = 20

            ws[status_cell] = status

        wb.save('goingout.xlsx')
        wb.close()

        return send_from_directory('../../', 'goingout.xlsx')
