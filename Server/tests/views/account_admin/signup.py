import unittest2 as unittest

from tests.views import account_admin

from server import app


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        self.access_token = account_admin.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_admin.remove_fake_account('chicken')

    def testA_createAccount(self):
        """
        TC about admin's account creating

        1. Check 'ID validation failed'
        2. Check 'signup succeed'
        3. Check 'login succeed'
        """
        rv = self.client.post('/admin/new-account', headers={'Authorization': self.access_token}, data={'id': 'fake_admin', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 204)
        # ID validation failed : already exists

        rv = self.client.post('/admin/new-account', headers={'Authorization': self.access_token}, data={'id': 'chicken', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 201)
        # Success

        rv = self.client.post('/admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 200)
        # Login test with created admin account
