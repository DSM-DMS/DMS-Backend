from datetime import datetime, time
import json
import unittest2 as unittest

from app.models.account import StudentModel
from tests.views.student import get_access_token

from server import app


class TestStay(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        StudentModel(
            id='fake',
            pw='9b2941f9e75a663a58d8f2102b3e40fab93e2a386471091cf64a80f32aa400fe',
            name='fake',
            number=1234
        ).save()

        self.access_token = get_access_token(self.client)

    def tearDown(self):
        StudentModel.objects(
            id='fake'
        ).delete()

    def testStay(self):
        rv = self.client.get('/stay', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)

        self.assertEqual(json.loads(rv.data.decode())['value'], 4)

        rv = self.client.post('/stay')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/stay', headers={'Authorization': self.access_token}, data={'value': 1})
        now = datetime.now()
        if (now.weekday() == 6 and now.time() > time(20, 30)) or (0 < now.weekday() < 3) or (now.weekday() == 3 and now.time() < time(22, 00)):
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/stay', headers={'Authorization': self.access_token})
            self.assertEqual(rv.status_code, 200)

            self.assertEqual(json.loads(rv.data.decode())['value'], 1)
        else:
            self.assertEqual(rv.status_code, 204)
