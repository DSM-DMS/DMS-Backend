from datetime import datetime

from app.models import *


class PointRuleModel(Document):
    """
    manages point rule
    """
    meta = {
        'collection': 'point_rule'
    }

    name = StringField(
        required=True
    )

    min_point = IntField(
        required=True,
        min_value=1
    )
    max_point = IntField(
        required=True,
        min_value=1
    )


class PointHistoryModel(EmbeddedDocument):
    """
    Dormitory good or bad point base
    """
    meta = {
        'collection': 'point_history'
    }

    time = DateTimeField(
        required=True,
        default=datetime.now()
    )

    reason = ReferenceField(
        document_type=PointRuleModel,
        required=True
    )
    point = IntField(
        required=True
    )
