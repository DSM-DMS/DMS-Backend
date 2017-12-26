import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.account import StudentModel
from app.models.meal import MealModel


class Meal(Resource):
    @jwt_required
    def get(self):
        """
        급식 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()

        if not student:
            return Response('', 403)

        date = request.args['date']

        meal = MealModel.objects(
            date=date
        ).first()

        if not meal:
            return Response('', 204)

        return Response(
            json.dumps(
                {
                    'breakfast': meal.breakfast,
                    'lunch': meal.lunch,
                    'dinner': meal.dinner
                },
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )
