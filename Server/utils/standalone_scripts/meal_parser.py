from schapi import SchoolAPI, Region

from app.models.meal import MealModel

api = SchoolAPI(Region.DAEJEON, 'G100000170')


def _parse(year, month):
    for index, meal in enumerate(api.get_monthly_menus(year, month)):
        MealModel(
            date='{0}-{1:02d}-{2:02d}'.format(year, month, index),
            breakfast=meal.breakfast or ['급식이 없습니다.'],
            lunch=meal.lunch or ['급식이 없습니다.'],
            dinner=meal.dinner or ['급식이 없습니다.']
        ).save()


if __name__ == '__main__':
    _parse(2018, 7)
