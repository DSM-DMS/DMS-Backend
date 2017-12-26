from datetime import datetime

from app.models import *


class PointBase(EmbeddedDocument):
    """
    Dormitory good or bad point base
    """
    meta = {
        'collection': 'point_base',
        'allow_inheritance': True
    }

    time = DateTimeField(
        required=True,
        default=datetime.now()
    )

    reason = StringField(
        required=True
    )
    point = IntField(
        required=True
    )


class GoodPointModel(PointBase):
    """
    Dormitory good point document
    """


class BadPointModel(PointBase):
    """
    Dormitory bad point document
    """
