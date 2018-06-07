from bson.objectid import ObjectId
from datetime import datetime

from mongoengine import *


class PointRuleModel(Document):
    """
    상벌점 규칙
    """
    meta = {
        'collection': 'point_rule'
    }

    name = StringField(
        required=True
    )
    # 규칙 이름

    point_type = BooleanField(
        required=True
    )
    # True : 상점, False : 벌점

    min_point = IntField(
        required=True
    )
    # 최소 점수

    max_point = IntField(
        required=True
    )
    # 최대 점수
    # point_type이 false(벌점)라면 해당 필드들도 음수


class PointHistoryModel(EmbeddedDocument):
    """
    각 학생에게 속해 있는(Embedded) 상벌점 내역
    """
    meta = {
        'collection': 'point_history'
    }

    id = ObjectIdField(
        primary_key=True,
        default=ObjectId
    )

    time = DateTimeField(
        default=datetime.now
    )
    # 상벌점을 부과한 시간

    reason = StringField(
        required=True
    )
    # 벌점 부과 사유

    point_type = BooleanField(
        required=True
    )
    # True : 상점, False : 벌점

    point = IntField(
        required=True
    )
    # 부과한 점수
