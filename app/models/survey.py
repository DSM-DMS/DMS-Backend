from datetime import date

from app.models import *
from app.models.account import StudentModel


class QuestionModel(EmbeddedDocumentField):
    """
    Each questions in a survey document
    """
    meta = {
        'collection': 'question'
    }

    survey_id = StringField(
        required=True
    )

    title = StringField(
        required=True
    )

    is_objective = BooleanField(
        required=True
    )

    choice_paper = ListField()

    answer = EmbeddedDocumentListField(
        document_type=AnswerModel,
        required=True
    )


class SurveyModel(Document):
    """
    Survey information document
    """
    meta = {
        'collection': 'survey'
    }

    title = StringField(
        required=True
    )

    start_date = StringField(
        required=True
    )

    end_date = StringField(
        required=True
    )

    target = ListField(
        IntField()
    )

    creation_date = DateTimeField(
        required=True,
        default=date.today()
    )

    question = EmbeddedDocumentListField(
        document_type=QuestionModel,
        required=True
    )


class AnswerModel(EmbeddedDocumentField):
    """
    Answer data for each question document
    """
    meta = {
        'collection': 'answer'
    }

    answer_student = ReferenceField(
        document_type=StudentModel
    )

    question = ReferenceField(
        document_type=QuestionModel
    )

    answer = StringField()