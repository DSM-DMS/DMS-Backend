import unittest

from tests.views import account_admin, account_student

from server import app


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_admin.remove_fake_account('chicken')
        account_student.remove_fake_account()

    def testA_createAccount(self):
        """
        TC about admin account creation

        - Preparations
        None

        - Exception Tests
        Already existing admin ID
        Forbidden with student access token

        - Process
        Create new admin account

        - Validation
        Test admin auth
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/new-account', headers={'Authorization': self.admin_access_token}, data={'id': 'fake_admin', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/admin/new-account', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/new-account', headers={'Authorization': self.admin_access_token}, data={'id': 'chicken', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.post('/admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)
        # -- Validation --
