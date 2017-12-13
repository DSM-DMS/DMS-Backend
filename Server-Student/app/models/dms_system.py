from datetime import date

from app.models.account import StudentModel
from app.models import *


class BugReportModel(Document):
    author = ReferenceField(StudentModel)
    title = StringField(required=True)
    content = StringField(required=True)

    report_date = StringField(required=True, default=str(date.today()))
