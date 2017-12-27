import unittest2 as unittest

from tests.views import admin

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        admin.create_fake_account()

    def tearDown(self):
        admin.remove_fake_account()
        admin.remove_fake_account('chicken')

    def testSignup(self):
        rv = self.client.post('/admin/new-account', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # Authorization failed

        access_token = admin.get_access_token(self.client)
        rv = self.client.post('/admin/new-account', headers={'Authorization': access_token}, data={'id': 'fake', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 400)
        # Bad request(missing parameter)

        rv = self.client.post('/admin/new-account', headers={'Authorization': access_token}, data={'id': 'fake', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 204)
        # ID validation failed

        rv = self.client.post('/admin/new-account', headers={'Authorization': access_token}, data={'id': 'chicken', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 201)
        # Success

        rv = self.client.post('/admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 200)
        # Login test
