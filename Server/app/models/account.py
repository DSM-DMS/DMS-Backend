from datetime import datetime

from app.models import *

from app.models.apply import ExtensionApplyModel, GoingoutApplyModel, StayApplyModel
from app.models.point import GoodPointModel, BadPointModel


class SignupWaitingModel(Document):
    """
    Data before the student's signup
    """
    meta = {
        'collection': 'signup_waiting',
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
    DMS account Base Document
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
    Student account document
    """
    meta = {
        'collection': 'student'
    }

    number = IntField(
        required=True
    )

    # afterschool_apply = EmbeddedDocumentField(
    #     document_type=AfterSchoolApplyModel
    # )

    extension_apply_11 = EmbeddedDocumentField(
        document_type=ExtensionApplyModel
    )

    extension_apply_12 = EmbeddedDocumentField(
        document_type=ExtensionApplyModel
    )

    goingout_apply = EmbeddedDocumentField(
        document_type=GoingoutApplyModel,
        default=GoingoutApplyModel()
    )

    stay_apply = EmbeddedDocumentField(
        document_type=StayApplyModel,
        default=StayApplyModel()
    )

    good_point = EmbeddedDocumentListField(
        document_type=GoodPointModel
    )

    bad_point = EmbeddedDocumentListField(
        document_type=BadPointModel
    )


class AdminModel(AccountBase):
    """
    Admin account document
    """
    meta = {
        'collection': 'admin'
    }


class RefreshTokenModel(Document):
    """
    Manages JWT refresh token
    """
    meta = {
        'collection': 'refresh_token'
    }

    token = UUIDField(
        primary_key=True
    )

    token_owner = ReferenceField(
        document_type=AccountBase,
        required=True
    )

    pw_snapshot = StringField(
        required=True
    )
