from bson.objectid import ObjectId

from app.models import *


class AfterSchoolItemModel(EmbeddedDocument):
    id = ObjectIdField(primary_key=True, default=ObjectId())
    title = StringField(required=True)
    on_monday = BooleanField(required=True, default=False)
    on_tuesday = BooleanField(required=True, default=False)
    on_saturday = BooleanField(required=True, default=False)
    target = ListField(IntField())


class AfterSchoolModel(Document):
    start_date = StringField(required=True)
    end_date = StringField(required=True)
    content = StringField(required=True)
    items = ListField(EmbeddedDocumentField(AfterSchoolItemModel))
