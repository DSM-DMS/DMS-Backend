from bson.objectid import ObjectId
from datetime import date

from app.models import *


class PointBase(EmbeddedDocument):
    """
    Dormitory good or bad point base
    """

    _id = ObjectIdField(
        required=True,
        default=ObjectId()
    )
    date = DateTimeField(
        required=True,
        default=date.today()
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
    meta = {
        'collection': 'good_point'
    }


class BadPointModel(PointBase):
    """
    Dormitory bad point document
    """
    meta = {
        'collection': 'bad_point'
    }
