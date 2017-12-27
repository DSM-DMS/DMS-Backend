import unittest2 as unittest

from app.models.account import AdminModel
from tests.views.admin import create_fake_account, get_access_token

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        create_fake_account()

    def tearDown(self):
        AdminModel.objects(
            id='fake'
        ).delete()
        AdminModel.objects(
            id='chicken'
        ).delete()

    def testSignup(self):
        rv = self.client.post('admin/signup', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # Authorization failed

        access_token = get_access_token(self.client)
        rv = self.client.post('admin/signup', headers={'Authorization': access_token}, data={'id': 'fake', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 400)
        # Bad request(missing parameter)

        rv = self.client.post('admin/signup', headers={'Authorization': access_token}, data={'id': 'fake', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 204)
        # ID validation failed

        rv = self.client.post('admin/signup', headers={'Authorization': access_token}, data={'id': 'chicken', 'pw': 'chicken', 'name': 'lover'})
        self.assertEqual(rv.status_code, 201)
        # Succss

        rv = self.client.post('admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 200)
        # Login test
