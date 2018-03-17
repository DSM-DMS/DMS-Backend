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

    point_type = BooleanField()

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
        primary_key=True
    )

    time = DateTimeField(
        required=True
    )

    reason = StringField(
        required=True
    )
    point_type = BooleanField()
    point = IntField(
        required=True
    )