import json
import unittest2 as unittest

from app.models.account import StudentModel
from tests.views.student import get_access_token, get_refresh_token

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        StudentModel(
            id='fake',
            pw='9b2941f9e75a663a58d8f2102b3e40fab93e2a386471091cf64a80f32aa400fe',
            name='fake',
            number=1234
        ).save()

    def tearDown(self):
        StudentModel.objects(
            id='fake'
        ).delete()

    def testAuth(self):
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
