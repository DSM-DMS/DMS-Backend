from datetime import date

from app.models.account import StudentModel
from app.models import *


class BugReportModel(Document):
    """
    Bug report document
    """
    meta = {
        'collection': 'bug_report'
    }

    report_date = DateTimeField(
        required=True,
        default=date.today()
    )

    informant = ReferenceField(
        document_type=StudentModel,
        required=True
    )

    title = StringField(
        required=True
    )

    content = StringField(
        required=True
    )
