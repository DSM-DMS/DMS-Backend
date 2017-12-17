from datetime import datetime

from app.models import *

from app.models.apply import *


class SignupWaitingModel(Document):
    """
    Data before the student's signup
    """
    meta = {
        'collection': 'signup_waiting',
        'max_documents': 240
    }

    uuid = UUIDField(
        primary_key=True,
    )
    name = StringField(
        required=True
    )
    number = IntField(
        required=True
    )


class AccountBase(Document):
    """
    DMS Account Base Document
    """
    meta = {
        'collection': 'account_base',
        'allow_inheritance': True
    }

    signup_date = DateTimeField(
        required=True,
        default=datetime.now()
    )

    id = StringField(
        primary_key=True,
    )
    pw = StringField(
        required=True
    )
    name = StringField(
        required=True
    )


class StudentModel(AccountBase):
    """
    Student Account
    """
    meta = {
        'collection': 'student'
    }

    number = IntField(
        required=True
    )

    afterschool_apply = EmbeddedDocumentField(
        document_type=AfterSchoolApplyModel
    )

    extension_apply_11 = EmbeddedDocumentField(
        document_type=ExtensionApplyModel
    )

    extension_apply_12 = EmbeddedDocumentField(
        document_type=ExtensionApplyModel
    )

    going_out_apply = EmbeddedDocumentField(
        document_type=GoingoutApplyModel,
        default=GoingoutApplyModel()
    )

    stay_apply = EmbeddedDocumentField(
        document_type=StayApplyModel,
        default=StayApplyModel()
    )


class AdminModel(AccountBase):
    """
    Admin Account
    """
    meta = {
        'collection': 'admin'
    }
