from flask import Blueprint, Response
from flask_restful import Api

from app.views import BaseResource
from utils.uuid_excel import uuid_excel_save

api = Api(Blueprint('uuid-excel-to-db-api', __name__))
api.prefix = '/system'


@api.resource('/uuid-excel-to-db')
class UUIDExcelToDB(BaseResource):
    def get(self):
        uuid_excel_save()
        return Response('', 201)