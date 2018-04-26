from datetime import datetime

from app.models import *
from app.models.account import StudentModel


class ApplyBase(Document):
    """
    신청 정보에 대한 상위 collection
    """
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    apply_date = DateTimeField(
        required=True,
        default=datetime.now()
    )
    # 신청 시간

    student = ReferenceField(
        document_type=StudentModel,
        required=True
    )
    # 신청 학생


class ExtensionApplyBase(ApplyBase):
    """
    연장 신청 정보에 대한 상위 collection
    의도적으로 11시 연장신청과 12시 연장신청을 구분하기 위해 사용
    """
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    class_ = IntField(
        required=True
    )
    # 연장신청 교실

    seat = IntField(
        required=True
    )
    # 자리


class ExtensionApply11Model(ExtensionApplyBase):
    """
    11시 연장 신청 정보
    """
    meta = {
        'collection': 'apply_extension_11'
    }


class ExtensionApply12Model(ExtensionApplyBase):
    """
    12시 연장 신청 정보
    """
    meta = {
        'collection': 'apply_extension_12'
    }


class GoingoutApplyModel(ApplyBase):
    """
    외출 신청 정보
    """
    meta = {
        'collection': 'apply_goingout'
    }

    on_saturday = BooleanField(
        required=True
    )
    on_sunday = BooleanField(
        required=True
    )


class StayApplyModel(ApplyBase):
    """
    잔류 신청 정보
    1 : 금요귀가
    2 : 토요귀가
    3 : 토요귀사
    4 : 잔류
    """
    meta = {
        'collection': 'apply_stay'
    }

    value = IntField(
        required=True
    )
