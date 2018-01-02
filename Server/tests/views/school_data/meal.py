import unittest2 as unittest

from app.models.meal import MealModel

from server import app


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()


    def tearDown(self):
        MealModel.objects(date='2001-04-20').delete()

    def testA_meal(self):
        """
        TC about getting meal
        
        - Preparations
        Add meal data in MealModel
        
        - Exception Tests
        No data in database
        
        - Process
        Get meal data
        
        - Validation
        Check meal data
        """
        # -- Preparation --
        # -- Preparation --

        # == Exception Tests --
        rv = self.client.get('/meal/2000-00-00')
        self.assertEqual(rv.status_code, 204)
        # == Exception Tests --

        # -- Process --
        rv = self.client.get('/meal/2001-04-20')
        self.assertEqual(rv.status_code, 200)
        # -- Process --
        # Success
