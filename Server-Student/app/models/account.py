from datetime import date

from app.models import *
from app.models.apply import AfterSchoolApplyModel, ExtensionApplyModel, GoingoutApplyModel, StayApplyModel


class SignupRequiredModel(Document):
    uuid = StringField(primary_key=True)
    name = StringField(required=True)
    number = IntField(required=True)


class AccountBase(Document):
    signup_date = StringField(required=True, default=str(date.today()))

    id = StringField(primary_key=True)
    pw = StringField(required=True)
    name = StringField(required=True)

    meta = {'allow_inheritance': True}


class StudentModel(AccountBase):
    number = IntField(required=True)
    afterschool_apply = EmbeddedDocumentField(AfterSchoolApplyModel)
    extension_apply_11 = EmbeddedDocumentField(ExtensionApplyModel)
    extension_apply_12 = EmbeddedDocumentField(ExtensionApplyModel)
    goingout_apply = EmbeddedDocumentField(GoingoutApplyModel, default=GoingoutApplyModel())
    # Default sat=False, sun=False
    stay_apply = EmbeddedDocumentField(StayApplyModel, default=StayApplyModel())
    # Default value=4


class AdminModel(AccountBase):
    pass


class RefreshTokenModel(Document):
    refresh_token = UUIDField(primary_key=True)
    owner = ReferenceField(AccountBase, required=True)
    pw_snapshot = StringField(required=True)
