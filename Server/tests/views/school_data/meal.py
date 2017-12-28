import unittest2 as unittest

from app.models.meal import MealModel

from server import app


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        MealModel(
            date='2001-04-20',
            breakfast=['2001년', '04월', '20일은'],
            lunch=['인상민이', '태어난', '날'],
            dinner=['기억해주세염', '!!!!']
        ).save()

    def tearDown(self):
        MealModel.objects(date='2001-04-20').delete()

    def testA_meal(self):
        """
        TC about getting meal
        
        1. Check no data on the day
        2. Check Success
        """
        rv = self.client.get('/meal/2000-00-00')
        self.assertEqual(rv.status_code, 204)
        # Check no data on the day

        rv = self.client.get('/meal/2001-04-20')
        self.assertEqual(rv.status_code, 200)
        # Success
