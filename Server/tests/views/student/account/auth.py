import json
import unittest2 as unittest

from app.models.account import StudentModel
from tests.views.student import create_fake_account, get_access_token, get_refresh_token

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        create_fake_account()

    def tearDown(self):
        StudentModel.objects(
            id='fake'
        ).delete()

    def testAuth(self):
        rv = self.client.post('/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # Login fail

        rv = self.client.post('/auth', data={'id': 'fake', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 200)
        # Success

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data and 'refresh_token' in data)
        # Token check

    def testRefresh(self):
        rv = self.client.post('/refresh')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        refresh_token = get_refresh_token(self.client)
        rv = self.client.post('/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 200)
        # Success

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data)
        # New access token check

        access_token = get_access_token(self.client)
        rv = self.client.post('/change/pw', headers={'Authorization': access_token}, data={'current_pw': 'fake', 'new_pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Change password

        rv = self.client.post('/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 205)
        # Refresh fail after password changed
