import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.survey.survey import *
from app.models.account import StudentModel
from app.models.survey import AnswerModel, QuestionModel, SurveyModel


class SurveyList(Resource):
    @swag_from(SURVEY_LIST_GET)
    @jwt_required
    def get(self):
        """
        설문조사 리스트 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        student_number = student.number

        return Response(
            json.dumps(
                [{
                    'id': str(survey.id),
                    'creation_time': str(survey.creation_time)[:-7],
                    'title': survey.title,
                    'start_date': str(survey.start_date),
                    'end_date': str(survey.end_date)
                } for survey in SurveyModel.objects if student_number in survey.target],
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )
        # Filter by student number


class Survey(Resource):
    @swag_from(SURVEY_GET)
    @jwt_required
    def get(self):
        """
        설문조사의 질문 리스트 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
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
            'choice_paper': question.choice_paper
        } for question in QuestionModel.objects(survey=survey)]

        for question in questions:
            answer = AnswerModel.objects(
                question=question,
                answer_student=student
            ).first()

            if answer:
                question['answer'] = answer.content
            else:
                question['answer'] = None

        return Response(
            json.dumps(
                questions,
                ensure_ascii=False
            ),
            200,
            content_type='application/json; charset=utf8'
        )

    @swag_from(SURVEY_POST)
    @jwt_required
    def post(self):
        """
        설문조사 답변 업로드
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        question_id = request.form['question_id']
        if len(question_id) != 24:
            return Response('', 204)

        question = QuestionModel.objects(
            id=question_id
        ).first()
        if not question:
            # Question doesn't exist
            return Response('', 204)

        answer = request.form['answer']

        AnswerModel.objects(
            question=question,
            answer_student=student
        ).delete()
        # Delete existing document

        AnswerModel(
            question=question,
            answer_student=student,
            answer=answer
        ).save()
        # Insert new answer data

        return Response('', 201)
