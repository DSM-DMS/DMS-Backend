from mongoengine import *


class MealModel(Document):
    """
    급식 정보
    """
    meta = {
        'collection': 'meal'
    }

    date = StringField(
        primary_key=True
    )
    breakfast = ListField(
        required=True
    )
    lunch = ListField(
        required=True
    )
    dinner = ListField(
        required=True
    )
