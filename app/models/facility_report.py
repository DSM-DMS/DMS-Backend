from datetime import date

from app.models import *
from app.models.account import StudentModel


class FacilityReportModel(Document):
    """
    Facility report document
    """
    meta = {
        'collection': 'facility_report'
    }

    report_date = DateTimeField(
        required=True,
        default=date.today()
    )

    informant = ReferenceField(
        document_type=StudentModel,
        required=True
    )

    room = IntField(
        required=True,
        min_value=200,
        max_value=599
    )

    title = StringField(
        required=True
    )

    content = StringField(
        required=True
    )
