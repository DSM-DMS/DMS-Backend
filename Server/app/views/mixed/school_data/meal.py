import json

from flasgger import swag_from
from flask import Blueprint, Response
from flask_restful import Api, Resource, abort

from app.docs.mixed.school_data.meal import *
from app.models.meal import MealModel

api = Api(Blueprint('meal-api', __name__))


@api.resource('/meal/<date>')
class Meal(Resource):
    @swag_from(MEAL_GET)
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

        return Response(json.dumps(response, ensure_ascii=False), content_type='application/json; charset=utf8')
