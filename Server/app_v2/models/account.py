from app_v2.models import *

from app_v2.models.point import PointHistoryModel


class SignupWaitingModel(Document):
    """
    Data before the student's signup
    """
    meta = {
        'collection': 'signup_waiting'
    }

    uuid = StringField(
        primary_key=True,
        min_length=4,
        max_length=4
    )
    # length limit 추가

    name = StringField(
        required=True
    )
    number = IntField(
        required=True,
        min_value=1101,
        max_value=3421
    )


class AccountBase(Document):
    """
    DMS account_admin Base Document
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }
    # collection claim 제거

    signup_time = DateTimeField(
        required=True
    )
    # required 추가

    id = StringField(
        primary_key=True
    )
    pw = StringField(
        required=True
    )
    name = StringField(
        required=True
    )


class StudentModel(AccountBase):
    """
    Student account model
    """
    meta = {
        'collection': 'account_student'
    }
    # meta 추가

    # --
    # apply 관련 EmbeddedDocumentField 제거
    # --

    number = IntField(
        required=True,
        min_value=1101,
        max_value=3421
    )

    good_point = IntField(
        default=0
    )

    bad_point = IntField(
        default=0
    )

    # point_histories = EmbeddedDocumentListField(
    #     document_type=PointHistoryModel,
    #     required=False
    # )

    penalty_training_status = BooleanField(
        required=True,
        default=False
    )

    penalty_level = IntField(
        required=True,
        default=0
    )


class AdminModel(AccountBase):
    """
    Admin account model
    """
    meta = {
        'collection': 'account_admin'
    }
    # meta 추가


class SystemModel(AccountBase):
    """
    System account model
    """
    meta = {
        'collection': 'account_system'
    }
    # meta 추가


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
        required=True,
        reverse_delete_rule=CASCADE
    )
    # reverse_delete_rule 추가
    pw_snapshot = StringField(
        required=True
    )
