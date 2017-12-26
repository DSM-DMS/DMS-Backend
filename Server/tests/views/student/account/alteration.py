import json
import unittest2 as unittest

from app.models.account import StudentModel
from tests.views.student import create_fake_account, get_access_token

from server import app


class TestAlteration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        create_fake_account()
        self.access_token = get_access_token(self.client)

    def tearDown(self):
        StudentModel.objects(
            id='fake'
        ).delete()

    def testChangePW(self):
        rv = self.client.post('/change/pw')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/change/pw', headers={'Authorization': self.access_token}, data={'current_pw': 'invalid'})
        self.assertEqual(rv.status_code, 403)
        # Invalid password

        rv = self.client.post('/change/pw', headers={'Authorization': self.access_token}, data={'current_pw': 'fake', 'new_pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Success

        rv = self.client.post('/auth', data={'id': 'fake', 'pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Auth check

    def testChangeNumber(self):
        rv = self.client.post('/change/number')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/change/number', data={'new_number': 2120}, headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        # Success

        rv = self.client.get('/mypage', headers={'Authorization': self.access_token})
        self.assertEqual(json.loads(rv.data.decode())['number'], 2120)
        # Number check
