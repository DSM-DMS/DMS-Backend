from app_v2.models import *


class ReportBase(Document):
    """
    Report document base
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }
    # collection claim 제거

    report_time = DateTimeField(
        required=True
    )

    # title 제거

    author = StringField(
        required=True
    )

    content = StringField(
        required=True
    )


class FacilityReportModel(ReportBase):
    """
    Facility report document
    """
    meta = {
        'collection': 'report_facility'
    }
    # collection name 변경

    room = IntField(
        required=True,
        min_value=200,
        max_value=519
    )
