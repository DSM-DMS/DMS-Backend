from schapi import SchoolAPI

from app.models.meal import MealModel

api = SchoolAPI(SchoolAPI.Region.DAEJEON, 'G100000170')


def parse(year, month):
    if MealModel.objects(date='{0}-{1:02d}-{2:02d}'.format(year, month, 1)):
        return

    for index, meal in enumerate(api.get_monthly_menus(year, month)):
        MealModel(
            date='{0}-{1:02d}-{2:02d}'.format(year, month, index),
            breakfast=meal.breakfast or ['급식이 없습니다.'],
            lunch=meal.lunch or ['급식이 없습니다.'],
            dinner=meal.dinner or ['급식이 없습니다.']
        ).save()
