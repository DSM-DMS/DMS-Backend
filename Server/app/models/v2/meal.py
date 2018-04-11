from app.models.v2 import *


class MealModel(Document):
    """
    School's meal document
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
