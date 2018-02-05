from openpyxl import load_workbook

from flask import Blueprint, Response
from flask_restful import Api

from app.models.account import SignupWaitingModel
from app.views import BaseResource

api = Api(Blueprint('uuid-excel-to-db-api', __name__))
api.prefix = '/system'


@api.resource('/uuid-excel-to-db')
class UUIDExcelToDB(BaseResource):
    def _uuid_excel_save(self):
        for i in range(1, 4):
            for j in range(1, 5):
                wb = load_workbook('uuid_{0}_{1}.xlsx'.format(i, j)).get_sheet_by_name('Sheet1')
                for k in range(2, 23):
                    if wb['A{0}'.format(k)].value:
                        SignupWaitingModel(
                            uuid=wb['C{0}'.format(k)].value,
                            name=wb['A{0}'.format(k)].value,
                            number=int(wb['B{0}'.format(k)].value)
                        ).save()

    def get(self):
        self._uuid_excel_save()
        return Response('', 201)
