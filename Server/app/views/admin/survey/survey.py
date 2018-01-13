import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.admin.survey.survey import *
from app.models.account import AdminModel
from app.models.survey import QuestionModel, SurveyModel


class SurveyManaging(Resource):
    @swag_from(SURVEY_MANAGING_GET)
    @jwt_required
    def get(self):
        """
        설문지 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        response = [{
            'id': str(survey.id),
            'creation_time': str(survey.creation_time)[:10],
            'title': survey.title,
            'description': survey.description,
            'start_date': str(survey.start_date),
            'end_date': str(survey.end_date)
        } for survey in SurveyModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @swag_from(SURVEY_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        설문지 등록
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        target = json.loads(request.form['target'])

        survey = SurveyModel(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            target=target
        ).save()

        return {
            'id': str(survey.id)
        }, 201

    @swag_from(SURVEY_MANAGING_DELETE)
    @jwt_required
    def delete(self):
        """
        설문지 제거
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        survey_id = request.form['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        survey.delete()

        return Response('', 200)


class QuestionManaging(Resource):
    @swag_from(QUESTION_MANAGING_GET)
    @jwt_required
    def get(self):
        """
        설문지의 질문 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        survey_id = request.args['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        response = [{
            'id': str(question.id),
            'title': question.title,
            'is_objective': question.is_objective,
            'choice_paper': question.choice_paper if question.is_objective else None
        } for question in QuestionModel.objects(survey=survey)]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @swag_from(QUESTION_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        설문지에 질문 등록
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        rq = request.json

        survey_id = rq['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        questions = rq['questions']
        ids = list()
        for question in questions:
            title = question['title']
            is_objective = question['is_objective']

            q = QuestionModel(
                survey=survey,
                title=title,
                is_objective=is_objective,
                choice_paper=question['choice_paper'] if is_objective else []
            ).save()

            ids.append(str(q.id))

        return ids, 201
