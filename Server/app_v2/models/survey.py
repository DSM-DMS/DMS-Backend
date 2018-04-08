from app_v2.models import *
from app_v2.models.account import StudentModel


class SurveyModel(Document):
    """
    Survey information document
    """
    meta = {
        'collection': 'survey'
    }
    # collection name 변경

    creation_time = DateTimeField(
        required=True
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


class QuestionModel(Document):
    """
    Each questions in a survey document
    """

    meta = {
        'collection': 'survey_question'
    }
    # collection name 변경

    survey = ReferenceField(
        document_type=SurveyModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    title = StringField(
        required=True
    )
    is_objective = BooleanField(
        required=True
    )
    choice_paper = ListField()


class AnswerModel(Document):
    """
    Answer data for each question document
    """

    meta = {
        'collection': 'survey_answer'
    }
    # collection name 변경

    question = ReferenceField(
        document_type=QuestionModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    answer_student = ReferenceField(
        document_type=StudentModel,
        required=True,
        reverse_delete_rule=CASCADE
    )
    # reverse_delete_rule 추가

    content = StringField(
        required=True
    )
