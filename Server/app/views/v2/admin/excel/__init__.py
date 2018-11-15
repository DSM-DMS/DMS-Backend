from openpyxl import Workbook

from flask import make_response, send_from_directory

from app.views.v2 import BaseResource

from utils.excel_style_manager import ready_applyment_worksheet


class ExcelDownload(BaseResource):
    def __init__(self, model, filename, extension='xlsx'):
        self.model = model
        self.filename = filename
        self.extension = extension
        self.filename_full = '{}.{}'.format(self.filename, self.extension)

        super(ExcelDownload, self).__init__()

    def ready_worksheet(self):
        wb = Workbook()
        ws = wb.active

        ready_applyment_worksheet(ws)

        return wb, ws

    def save_excel(self, wb):
        wb.save('{}'.format(self.filename_full))
        wb.close()

    def get_response_object_with_excel_file(self):
        resp = make_response(send_from_directory('../', self.filename_full))
        resp.headers.extend({'Cache-Control': 'no-cache'})

        return resp

    def get_status(self, apply):
        raise NotImplementedError()

    employed = [3101, 3102, 3105, 3106, 3111, 3113, 3114, 3116, 3118,
                3201, 3202, 3203, 3206, 3207, 3208, 3209, 3210, 3211, 3212, 3213, 3215, 3217,
                3301, 3302, 3303, 3304, 3305, 3306, 3307, 3309, 3310, 3313, 3314, 3318,
                3404, 3408, 3409, 3410, 3411, 3414, 3415]
