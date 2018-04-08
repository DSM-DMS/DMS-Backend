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


class BugReportModel(ReportBase):
    """
    Bug report document
    
    platform
    1 : Web
    2 : Android
    3 : IOS
    """
    meta = {
        'collection': 'report_bug'
    }
    # collection name 변경

    platform_type = IntField(
        required=True,
        min_value=1,
        max_value=3
    )
    # platform_type 추가


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
