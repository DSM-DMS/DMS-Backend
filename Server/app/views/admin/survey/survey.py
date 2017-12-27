from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.admin.survey.survey import *
from app.models.account import AdminModel
from app.models.survey import QuestionModel, SurveyModel


class AdminSurvey(Resource):
    @swag_from(SURVEY_POST)
    @jwt_required
    def post(self):
        """
        설문조사지 등록
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        target = list(request.form['target'])

        SurveyModel(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            target=target
        ).save()

        return Response('', 201)


class AdminSurveyQuestion(Resource):
    @swag_from(QUESTION_POST)
    @jwt_required
    def post(self):
        """
        설문조사에 질문 등록
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        id = request.form['id']
        title = request.form['title']
        is_objective = request.form.get('is_objective')

        if not SurveyModel.objects(id=id).first():
            return Response('', 204)

        if is_objective:
            choice_paper = list(request.form['choice_paper'])

            QuestionModel(
                survey_id=id,
                title=title,
                is_objective=True,
                choice_paper=choice_paper
            ).save()
        else:
            QuestionModel(
                survey_id=id,
                title=title,
                is_objective=False
            ).save()

        return Response('', 201)
