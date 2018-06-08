from datetime import datetime
import time

from mongoengine import *

from config import Config
connect(**Config.MONGODB_SETTINGS)

from app.models.account import StudentModel
from app.models.point import PointHistoryModel
from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel


if 0 < datetime.now().time().hour < 12:
    ExtensionApply11Model.objects.delete()
    ExtensionApply12Model.objects.delete()


def clear_duplicated_apply_data(student, model):
    applies = model.objects(student=student)
    if applies.count() >= 2:
        print(student.number, student.name, '{} {}개'.format(model.__name__, goingout_applies.count()))

        applies.order_by('apply_date')[0:applies.count() - 1].delete()


for student in StudentModel.objects.order_by('number'):
    clear_duplicated_apply_data(student, GoingoutApplyModel)
    clear_duplicated_apply_data(student, StayApplyModel)
