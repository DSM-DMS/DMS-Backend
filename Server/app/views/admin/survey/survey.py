import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.admin.survey.survey import *
from app.models.account import AdminModel
from app.models.survey import QuestionModel, SurveyModel


class AdminSurvey(Resource):
    @jwt_required
    def get(self):
        """
        설문지 리스트 조회
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        return Response(
            json.dumps(
                [{
                    'id': str(survey.id),
                    'creation_time': str(survey.creation_time)[:-7],
                    'description': survey.description,
                    'title': survey.title,
                    'start_date': str(survey.start_date),
                    'end_date': str(survey.end_date)
                } for survey in SurveyModel.objects],
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )

    @swag_from(SURVEY_POST)
    @jwt_required
    def post(self):
        """
        설문지 등록
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

    @jwt_required
    def delete(self):
        """
        설문지 제거
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        survey_id = request.form['survey_id']

        survey = SurveyModel.objects(id=survey_id).first()

        if not survey:
            return Response('', 204)

        survey.delete()

        return Response('', 200)


class AdminQuestion(Resource):
    @jwt_required
    def get(self):
        """
        설문지의 질문 리스트 조회
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        survey_id = request.args['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(
            id=survey_id
        ).first()
        if not survey:
            # Survey doesn't exist
            return Response('', 204)

        questions = [{
            'id': str(question.id),
            'title': question.title,
            'is_objective': question.is_objective,
            'choice_paper': question.choice_paper if question.is_objective else None
        } for question in QuestionModel.objects(survey=survey)]

        return Response(
            json.dumps(
                questions,
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )

    @swag_from(QUESTION_POST)
    @jwt_required
    def post(self):
        """
        설문지에 질문 등록
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        survey_id = request.form['survey_id']
        title = request.form['title']
        is_objective = request.form.get('is_objective')

        if not SurveyModel.objects(survey_id=survey_id).first():
            return Response('', 204)

        if is_objective:
            choice_paper = list(request.form['choice_paper'])

            QuestionModel(
                survey_id=survey_id,
                title=title,
                is_objective=True,
                choice_paper=choice_paper
            ).save()
        else:
            QuestionModel(
                survey_id=survey_id,
                title=title,
                is_objective=False
            ).save()

        return Response('', 201)
