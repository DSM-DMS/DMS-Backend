from datetime import date

from app.models import *
from app.models.account import StudentModel


class FacilityReportModel(Document):
    informant = ReferenceField(StudentModel)
    title = StringField(required=True)
    room = IntField(required=True)
    content = StringField(required=True)

    report_date = StringField(required=True, default=str(date.today()))
