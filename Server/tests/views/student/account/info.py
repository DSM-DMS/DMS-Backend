import json
import unittest2 as unittest

from app.models.account import StudentModel
from tests.views.student import get_access_token

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

    def testMypage(self):
        rv = self.client.get('/mypage')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        access_token = get_access_token(self.client)

        rv = self.client.get('/mypage', headers={'Authorization': access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue('name' in data)
        self.assertEqual(data['name'], 'fake')
        self.assertTrue('number' in data)
        self.assertEqual(data['number'], 1234)

        self.assertTrue('extension_11' in data)
        self.assertEqual(data['extension_11']['class'], None)
        self.assertEqual(data['extension_11']['seat'], None)
        self.assertTrue('extension_12' in data)
        self.assertEqual(data['extension_12']['class'], None)
        self.assertEqual(data['extension_12']['seat'], None)

        self.assertTrue('goingout' in data)
        self.assertEqual(data['goingout']['sat'], None)
        self.assertEqual(data['goingout']['sun'], None)

        self.assertEqual(data['stay_value'], 4)
