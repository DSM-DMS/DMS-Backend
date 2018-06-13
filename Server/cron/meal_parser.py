from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))
sys.path.append(os.path.abspath(os.path.join('..', 'app')))

from mongoengine import *

from config import Config

from schapi import SchoolAPI

from app.models.meal import MealModel

api = SchoolAPI(SchoolAPI.Region.DAEJEON, 'G100000170')

connect(**Config.MONGODB_SETTINGS)


def _parse(year, month):
    if MealModel.objects(date='{}-{:0>2}-{:0>2}'.format(year, month, 1)):
        return

    for index, meal in enumerate(api.get_monthly_menus(year, month)):
        if not index:
            continue

        MealModel(
            date='{}-{:0>2}-{:0>2}'.format(year, month, index),
            breakfast=meal.breakfast or ['급식이 없습니다.'],
            lunch=meal.lunch or ['급식이 없습니다.'],
            dinner=meal.dinner or ['급식이 없습니다.']
        ).save()


today = datetime.now().date()
_parse(today.year, today.month)

a_month_after = today + timedelta(days=30)
_parse(a_month_after.year, a_month_after.month)
