from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.excel.goingout import *
from app.models.account import AdminModel
from app.models.apply import GoingoutApplyModel, StayApplyModel
from app.views.v2 import auth_required
from app.views.v2.admin.excel import ExcelDownload

from utils.excel_style_manager import get_cell_positions_from_student_number

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/excel/goingout'))


@api.resource('')
class GoingoutExcelDownload(ExcelDownload):
    def __init__(self):
        self.model = GoingoutApplyModel
        self.filename = 'goingout'

        super(GoingoutExcelDownload, self).__init__(self.model, self.filename)

    def get_status(self, apply):
        if apply.on_saturday and apply.on_sunday:
            return '토요일, 일요일 외출'
        elif apply.on_saturday:
            return '토요일 외출'
        elif apply.on_sunday:
            return '일요일 외출'
        else:
            return ''

    def generate_excel(self):
        wb, ws = self.ready_worksheet()

        for apply in self.model.objects:
            student = apply.student

            number_cell, name_cell, status_cell = get_cell_positions_from_student_number(student)

            stay_apply = StayApplyModel.objects(student=student).first()

            if stay_apply.value < 3:
                ws[number_cell] = None
                ws[name_cell] = None
                continue
            else:
                ws[number_cell] = student.number
                ws[name_cell] = student.name

            ws.column_dimensions['D'].width = 20
            ws.column_dimensions['H'].width = 20
            ws.column_dimensions['L'].width = 20
            ws.column_dimensions['P'].width = 20

            ws[status_cell] = self.get_status(apply)

        self.save_excel(wb)

    @auth_required(AdminModel)
    @swag_from(GOINGOUT_EXCEL_DOWNLOAD_GET)
    def get(self):
        """
        외출신청 정보 엑셀 다운로드
        """
        self.generate_excel()

        return self.get_response_object_with_excel_file()
