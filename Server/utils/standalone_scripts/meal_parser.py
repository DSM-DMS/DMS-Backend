from mongoengine import connect

from schapi import SchoolAPI

from app.models.meal import MealModel

api = SchoolAPI(SchoolAPI.Region.DAEJEON, 'G100000170')


def _parse(year, month):
    for index, meal in enumerate(api.get_monthly_menus(year, month)):
        MealModel(
            date='{0}-{1:02d}-{2:02d}'.format(year, month, index),
            breakfast=meal.breakfast or ['급식이 없습니다.'],
            lunch=meal.lunch or ['급식이 없습니다.'],
            dinner=meal.dinner or ['급식이 없습니다.']
        ).save()


if __name__ == '__main__':
    connect('dms-v2', host='dsm2015.cafe24.com', username='dms-v2', password='mountaindew')

    _parse(2018, 6)
