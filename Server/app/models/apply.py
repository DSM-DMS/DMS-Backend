from datetime import datetime

from app.models import *


class ApplyBase(EmbeddedDocument):
    """
    Apply data of student base document
    """
    meta = {
        'allow_inheritance': True
    }

    apply_date = DateTimeField(
        required=True,
        default=datetime.now()
    )


class ExtensionApplyModel(ApplyBase):
    """
    Extension apply data of student document includes 11st, 12nd extension apply
    """
    class_ = IntField(
        required=True
    )
    seat = IntField(
        required=True
    )


class GoingoutApplyModel(ApplyBase):
    """
    Goingout apply data of student document
    """
    on_saturday = BooleanField(
        required=True,
        default=False
    )
    on_sunday = BooleanField(
        required=True,
        default=False
    )


class StayApplyModel(ApplyBase):
    """
    Stay apply data of student document
    1 : Friday homecoming
    2 : Saturday homecoming
    3 : Saturday dormitory coming
    4 : Stay
    """
    value = IntField(
        required=True,
        default=4
    )
