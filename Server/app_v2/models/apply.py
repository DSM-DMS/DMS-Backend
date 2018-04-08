from app_v2.models import *
from app_v2.models.account import StudentModel


class ApplyBase(Document):
    # EmbeddedDocument -> Document
    """
    Apply data of student base document
    """
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }
    # abstract: True 추가

    student = ReferenceField(
        document_type=StudentModel,
        required=True
    )
    # EmbeddedDocument를 Document로 변경했으므로 ReferenceField 추가

    apply_date = DateTimeField(
        required=True
    )


class ExtensionApplyBase(ApplyBase):
    # Extension Apply 11, 12를 분리하기 위한 클래스
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    class_ = IntField(
        required=True
    )
    seat = IntField(
        required=True
    )


class ExtensionApply11Model(ExtensionApplyBase):
    meta = {
        'collection': 'apply_extension_11'
    }


class ExtensionApply12Model(ExtensionApplyBase):
    meta = {
        'collection': 'apply_extension_12'
    }


class GoingoutApplyModel(ApplyBase):
    """
    Goingout apply data of student document
    """
    meta = {
        'collection': 'apply_goingout'
    }

    on_saturday = BooleanField(
        required=True,
        default=False
    )
    on_sunday = BooleanField(
        required=True,
        default=False
    )


class StayApplyModel(ApplyBase):
    """
    Stay apply data of student document
    1 : Friday homecoming
    2 : Saturday homecoming
    3 : Saturday dormitory coming
    4 : Stay
    """
    meta = {
        'collection': 'apply_stay'
    }

    value = IntField(
        required=True,
        default=4
    )
