from datetime import datetime

from app.models import *
from app.models.account import StudentModel


class AnswerModel(EmbeddedDocument):
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
    content = StringField(
        required=True
    )


class QuestionModel(EmbeddedDocument):
    """
    Each questions in a survey document
    """
    meta = {
        'collection': 'question'
    }

    title = StringField(
        required=True
    )
    is_objective = BooleanField(
        required=True
    )
    choice_paper = ListField()
    answers = EmbeddedDocumentListField(
        document_type=AnswerModel
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
        default=datetime.now()
    )
    title = StringField(
        required=True
    )
    description = StringField(
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
        document_type=QuestionModel
    )
