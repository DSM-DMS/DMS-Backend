from datetime import date

from schapi import DAEJEON, SchoolAPI

from app.models.meal import MealModel

api = SchoolAPI(DAEJEON, 'G100000170')


def _parse(year, month):
    for index, meal in enumerate(api.get_monthly(year, month)):
        MealModel(
            date='{0}-{1:02d}-{2:02d}'.format(year, month, index),
            breakfast=meal.pop('breakfast', ['급식이 없습니다.']),
            lunch=meal.pop('lunch', ['급식이 없습니다.']),
            dinner=meal.pop('dinner', ['급식이 없습니다.'])).save()


def parse():
    today = date.today()
    year = today.year

    for month in range(1, 13):
        # Parse current year
        if not MealModel.objects(date='{0}-{1:02d}-01'.format(year, month, 1)):
            # Not parsed
            _parse(year, month)

            print('Parsed {0}-{1:02d}'.format(year, month))
