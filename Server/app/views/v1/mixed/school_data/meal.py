from flask import Blueprint, Response
from flask_restful import Api

from app.views.v1 import BaseResource


from app.models.meal import MealModel

api = Api(Blueprint('meal-api', __name__))


@api.resource('/meal/<date>')
class Meal(BaseResource):

    def get(self, date):
        """
        급식 조회
        """
        meal = MealModel.objects(date=date).first()
        if not meal:
            return Response('', 204)

        response = {
            'breakfast': meal.breakfast,
            'lunch': meal.lunch,
            'dinner': meal.dinner
        }

        return self.unicode_safe_json_response(response)
