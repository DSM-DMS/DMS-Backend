import unittest

from tests.views import account_student

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_student.create_fake_account()
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_student.remove_fake_account()

    def testA_auth(self):
        """
        TC about student authentication

        - Preparations
        None

        - Exception Tests
        Incorrect ID or PW

        - Process
        Auth

        - Validation
        Check response data
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/auth', data={'id': 'fake_student', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        self.assertTrue(rv.data)
        # -- Validation --

    def testB_refresh(self):
        """
        TC about student account refresh

        - Preparations
        Get refresh token using sample student account

        - Exception Tests
        Refresh fail after password changed

        - Process
        Refresh account

        - Validation
        Check response data
        """
        # -- Preparations --
        refresh_token = account_student.get_refresh_token(self.client)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/change/pw', headers={'Authorization': self.student_access_token}, data={'current_pw': 'fake', 'new_pw': 'new'})
        self.assertEqual(rv.status_code, 200)

        rv = self.client.post('/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 205)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/change/pw', headers={'Authorization': self.student_access_token}, data={'current_pw': 'new', 'new_pw': 'fake'})
        self.assertEqual(rv.status_code, 200)

        rv = self.client.post('/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        self.assertTrue(rv.data)
        # -- Validation --
