from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.excel.stay import *
from app.models.account import AdminModel
from app.models.apply import StayApplyModel
from app.views.v2 import auth_required
from app.views.v2.admin.excel import ExcelDownload

from utils.excel_style_manager import get_cell_positions_from_student_number

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/excel/stay'


@api.resource('')
class StayExcelDownload(ExcelDownload):
    def __init__(self):
        self.model = StayApplyModel
        self.filename = 'stay'

        super(StayExcelDownload, self).__init__(self.model, self.filename)

    def get_status(self, apply):
        if not apply or apply.value == 4:
            return '잔류'
        elif apply.value == 1:
            return '금요 귀가'
        elif apply.value == 2:
            return '토요 귀가'
        elif apply.value == 3:
            return '토요 귀사'
        else:
            return '잔류'

    def generate_excel(self):
        wb, ws = self.ready_worksheet()

        for apply in self.model.objects:
            student = apply.student

            if student.number in self.employed:
                continue

            number_cell, name_cell, status_cell = get_cell_positions_from_student_number(student)

            ws[number_cell] = student.number
            ws[name_cell] = student.name

            apply = StayApplyModel.objects(student=student).first()

            ws[status_cell] = self.get_status(apply)

        self.save_excel(wb)

    @auth_required(AdminModel)
    @swag_from(STAY_EXCEL_DOWNLOAD_GET)
    def get(self):
        """
        잔류신청 정보 엑셀 다운로드
        """
        self.generate_excel()

        return self.get_response_object_with_excel_file()
