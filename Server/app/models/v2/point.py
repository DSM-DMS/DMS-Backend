from app.models.v2 import *


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

    point_type = BooleanField(
        required=True
    )
    # required 추가

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

    # 필드 명을 다른 도큐먼트의 DateTimeField 처럼 ooo_time으로 네이밍 하는 것이 좋을 듯 ex) point_time, get_point_time
    time = DateTimeField(
        required=True
    )

    reason = StringField(
        required=True
    )

    point_type = BooleanField(
        required=True
    )
    # required 추가

    point = IntField(
        required=True
    )
