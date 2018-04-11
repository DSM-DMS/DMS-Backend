from datetime import datetime

from app.models.v2 import *


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
        required=True,
        min_value=0
    )
    # 최소 점수

    max_point = IntField(
        required=True,
        min_value=0
    )
    # 최대 점수


class PointHistoryModel(EmbeddedDocument):
    """
    각 학생에게 속해 있는(Embedded) 상벌점 내역
    """
    meta = {
        'collection': 'point_history'
    }

    id = ObjectIdField(
        primary_key=True,
        # default=ObjectId()
        # TODO 계정과 apply의 time에 대한 default 관련 이슈가 생기지 않으면 주석 제거
    )

    creation_time = DateTimeField(
        required=True,
        default=datetime.now()
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
