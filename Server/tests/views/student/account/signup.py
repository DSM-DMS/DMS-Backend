import json
import unittest2 as unittest
import uuid as u

from app.models.account import SignupWaitingModel, StudentModel
from tests.views.student import get_access_token

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.uuid = u.uuid4()

        SignupWaitingModel(
            uuid=self.uuid,
            name='new',
            number=12345
        ).save()

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

    def testIDVerify(self):
        rv = self.client.post('/verify/id', data={'id': 'fake'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/verify/id', data={'id': 'doesntexist'})
        self.assertEqual(rv.status_code, 200)

    def testUUIDVerify(self):
        rv = self.client.post('/verify/uuid', data={'uuid': str(u.uuid4())})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/verify/uuid', data={'uuid': str(self.uuid)})
        self.assertEqual(rv.status_code, 200)

    def testSignup(self):
        rv = self.client.post('/signup', data={'uuid': str(u.uuid4()), 'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 205)
        # UUID validation failed

        rv = self.client.post('/signup', data={'uuid': str(self.uuid), 'id': 'fake', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 204)
        # ID validation failed

        rv = self.client.post('/signup', data={'uuid': str(self.uuid), 'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 201)
        # Success

        access_token = get_access_token(self.client, 'doesntexist', 'fake')

        rv = self.client.get('/mypage', headers={'Authorization': access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue('name' in data)
        self.assertEqual(data['name'], 'new')
        self.assertTrue('number' in data)
        self.assertEqual(data['number'], 12345)

        StudentModel.objects(
            id='doesntexist'
        ).delete()