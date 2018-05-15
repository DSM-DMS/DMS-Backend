from datetime import datetime

from mongoengine import *


class ReportBase(Document):
    """
    신고 정보에 대한 상위 collection
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    report_time = DateTimeField(
        required=True,
        default=datetime.now
    )

    author = StringField(
        required=True
    )

    content = StringField(
        required=True
    )


class FacilityReportModel(ReportBase):
    """
    시설 고장 신고
    """
    meta = {
        'collection': 'report_facility'
    }

    room = IntField(
        required=True,
        min_value=200,
        max_value=519
    )
    # 호실
