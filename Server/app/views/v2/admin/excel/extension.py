from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.excel.extension import *
from app.models.account import AdminModel
from app.models.apply import ExtensionApply11Model, ExtensionApply12Model
from app.views.v2 import auth_required
from app.views.v2.admin.excel import ExcelDownload

from utils.excel_style_manager import get_cell_positions_from_student_number

api = Api(Blueprint(__name__, __name__, url_prefix='/admin/extension'))


class ExtensionExcelDownload(ExcelDownload):
    def __init__(self, *args, **kwargs):
        self.EXTENSION_CLASSES = '가온실', '나온실', '다온실', '라온실', '3층', '4층', '5층', '2층'

        super(ExtensionExcelDownload, self).__init__(*args, **kwargs)

    def generate_excel(self):
        wb, ws = self.ready_worksheet()

        for apply in self.model.objects:
            student = apply.student

            number_cell, name_cell, status_cell = get_cell_positions_from_student_number(student)

            ws[number_cell] = student.number
            ws[name_cell] = student.name
            ws[status_cell] = self.EXTENSION_CLASSES[apply.class_ - 1]

        self.save_excel(wb)


@api.resource('/11')
class Extension11ExcelDownload(ExtensionExcelDownload):
    def __init__(self):
        super(Extension11ExcelDownload, self).__init__(ExtensionApply11Model, '11')

    @auth_required(AdminModel)
    @swag_from(EXTENSION_11_EXCEL_DOWNLOAD_GET)
    def get(self):
        """
        11시 연장신청 정보 엑셀 다운로드
        """
        self.generate_excel()

        return self.get_response_object_with_excel_file()


@api.resource('/12')
class Extension12ExcelDownload(ExtensionExcelDownload):
    def __init__(self):
        super(Extension12ExcelDownload, self).__init__(ExtensionApply12Model, '12')

    @auth_required(AdminModel)
    @swag_from(EXTENSION_12_EXCEL_DOWNLOAD_GET)
    def get(self):
        """
        12시 연장신청 정보 엑셀 다운로드
        """
        self.generate_excel()

        return self.get_response_object_with_excel_file()
