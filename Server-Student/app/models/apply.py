from datetime import date

from app.models import *


class ApplyBase(EmbeddedDocument):
    apply_date = StringField(required=True, default=str(date.today()))
    meta = {'allow_inheritance': True}


class AfterSchoolApplyModel(ApplyBase):
    applied = ListField(StringField())
    # ReferenceField에서 EmbeddedDocument인 AfterSchoolItemModel 참조 불가


class ExtensionApplyModel(ApplyBase):
    class_ = IntField(required=True)
    seat = IntField(required=True)


class GoingoutApplyModel(ApplyBase):
    on_saturday = BooleanField(required=True, default=False)
    on_sunday = BooleanField(required=True, default=False)


class StayApplyModel(ApplyBase):
    value = IntField(required=True, default=4)
