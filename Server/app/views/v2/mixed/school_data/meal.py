from flask import Blueprint, Response
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.mixed.school_data.meal import *
from app.views.v2 import BaseResource
from app.models.meal import MealModel

api = Api(Blueprint(__name__, __name__))
api.prefix = '/meal'


@api.resource('/<date>')
class Meal(BaseResource):
    @swag_from(MEAL_GET)
    def get(self, date):
        meal = MealModel.objects(date=date).first()

        return self.unicode_safe_json_dumps({
            'breakfast': meal.breakfast,
            'lunch': meal.lunch,
            'dinner': meal.dinner
        }) if meal else Response('', 204)
