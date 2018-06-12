from datetime import datetime

from mongoengine import *

from config import Config

from app.models.account import StudentModel
from app.models.point import PointHistoryModel
from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel

connect(**Config.MONGODB_SETTINGS)


if 0 < datetime.now().time().hour < 12:
    ExtensionApply11Model.objects.delete()
    ExtensionApply12Model.objects.delete()


def clear_duplicated_apply_data(student, model):
    applies = model.objects(student=student)
    if applies.count() >= 2:
        print(student.number, student.name, '{} {}개'.format(model.__name__, model.count()))

        applies.order_by('apply_date')[0:applies.count() - 1].delete()


def insert_default_apply_data(student):
    if not GoingoutApplyModel.objects(student=student):
        GoingoutApplyModel(
            student=student,
            on_saturday=False,
            on_sunday=False
        ).save()

    if not StayApplyModel.objects(student=student):
        StayApplyModel(
            student=student,
            value=4
        ).save()


for student in StudentModel.objects.order_by('number'):
    clear_duplicated_apply_data(student, GoingoutApplyModel)
    clear_duplicated_apply_data(student, StayApplyModel)
    insert_default_apply_data(student)
