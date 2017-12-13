from app.models import *
from app.models.account import StudentModel


class ReportModel(Document):
    author = ReferenceField(StudentModel, required=True)
    title = StringField(required=True)
    room = IntField(required=True)
    content = StringField(required=True)
