import json

from flasgger import swag_from
from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from app.docs.mixed.school_data.meal import *
from app.models.account import AdminModel, StudentModel
from app.models.meal import MealModel


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

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')
