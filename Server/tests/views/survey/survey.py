import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestSurvey(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()

        self.admin_access_token = account_admin.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_addSurvey(self):
        """
        TC about survey addition

        - Purpose
        Test to add survey

        - Preparations
        None

        - Validation
        Check survey data using flag
        """

    def testB_deleteSurvey(self):
        """
        TC about survey deletion

        - Purpose
        Test to delete survey

        - Preparations
        Add sample survey data and take survey ID

        - Validation
        Check survey data length is 0
        """

    def testC_addQuestion(self):
        """
        TC about survey question addition

        - Purpose
        Test to add question

        - Preparations
        Add sample survey data and take survey ID

        - Validation
        Check question data with survey using flag
        """

    def testD_answer(self):
        """
        TC about survey answer upload

        - Purpose
        Test to answer question

        - Preparations
        Add sample survey, question data, and take question IDs

        - Validation
        Check answer data(API required)
        """
