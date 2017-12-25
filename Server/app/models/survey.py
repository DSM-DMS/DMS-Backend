from bson.objectid import ObjectId
from datetime import date

from app.models import *
from app.models.account import StudentModel


class AnswerModel(EmbeddedDocumentField):
    """
    Answer data for each question document
    """
    meta = {
        'collection': 'answer'
    }

    answer_student = ReferenceField(
        document_type=StudentModel,
        required=True
    )

    answer = StringField(
        required=True
    )


class QuestionModel(EmbeddedDocumentField):
    """
    Each questions in a survey document
    """
    meta = {
        'collection': 'question'
    }

    survey_id = ObjectIdField(
        primary_key=True,
        default=ObjectId()
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

    creation_time = DateTimeField(
        required=True,
        default=date.today()
    )

    title = StringField(
        required=True
    )

    start_date = DateTimeField(
        required=True
    )

    end_date = DateTimeField(
        required=True
    )

    target = ListField(
        IntField()
    )

    questions = EmbeddedDocumentListField(
        document_type=QuestionModel,
        required=True
    )
