from datetime import datetime

from app.models import *


class SurveyModel(Document):
    """
    설문지
    """
    meta = {
        'collection': 'survey'
    }

    creation_time = DateTimeField(
        required=True,
        default=datetime.now
    )
    # 설문지 생성 시간

    title = StringField(
        required=True
    )

    description = StringField(
        required=True
    )

    start_date = DateTimeField(
        required=True
    )
    # 설문의 시작 시간
    end_date = DateTimeField(
        required=True
    )
    # 설문의 종료 시간

    target = ListField(
        IntField()
    )
    # 설문 대상 학년


class QuestionModel(Document):
    """
    각 설문지에 대한 질문
    """
    meta = {
        'collection': 'survey_question'
    }

    survey = ReferenceField(
        document_type='SurveyModel',
        required=True,
        reverse_delete_rule=CASCADE
    )
    # 할당된 설문지

    title = StringField(
        required=True
    )
    is_objective = BooleanField(
        required=True
    )
    # 객관식 여부

    choice_paper = ListField()
    # 객관식일 경우 선택지


class AnswerModel(Document):
    """
    질문에 대한 답변
    """
    meta = {
        'collection': 'survey_answer'
    }

    question = ReferenceField(
        document_type='QuestionModel',
        required=True,
        reverse_delete_rule=CASCADE
    )
    # 할당된 질문

    answer_student = ReferenceField(
        document_type='StudentModel',
        required=True,
        reverse_delete_rule=CASCADE
    )
    # 답변 학생

    content = StringField(
        required=True
    )
