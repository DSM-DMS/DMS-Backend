import unittest2 as unittest

from tests.views import admin

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        admin.create_fake_account()
        self.access_token = admin.get_access_token(self.client)

    def tearDown(self):
        admin.remove_fake_account()
        admin.remove_fake_account('chicken')

    def testA_signup(self):
        """
        TC about admin's signup

        1. Check 'unauthorized'
        2. Check 'ID validation failed'
        3. Check 'signup succeed'
        4. Check 'login succeed'
        """
        rv = self.client.post('/admin/new-account', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # Authorization failed

        rv = self.client.post('/admin/new-account', headers={'Authorization': self.access_token}, data={'id': 'fake', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 204)
        # ID validation failed

        rv = self.client.post('/admin/new-account', headers={'Authorization': self.access_token}, data={'id': 'chicken', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 201)
        # Success

        rv = self.client.post('/admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 200)
        # Login test
