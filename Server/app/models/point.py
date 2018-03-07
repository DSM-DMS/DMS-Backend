from bson import ObjectId

from app.models import *


class PointRuleModel(Document):
    """
    Point rules
    """
    meta = {
        'collection': 'point_rule'
    }

    name = StringField(
        required=True
    )

    min_point = IntField(
        required=True
    )

    max_point = IntField(
        required=True
    )


class PointHistoryModel(EmbeddedDocument):
    """
    Good/bad point in dormitory of each students
    """
    meta = {
        'collection': 'point_history'
    }

    id = ObjectIdField(
        primary_key=True,
        default=ObjectId()
    )

    time = DateTimeField(
        required=True
    )

    reason = StringField(
        required=True
    )
    point = IntField(
        required=True
    )
