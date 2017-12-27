import json
import unittest2 as unittest
import uuid as u

from app.models.account import SignupWaitingModel
from tests.views import account_student

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        account_student.create_fake_account()
        self.uuid = u.uuid4()

        SignupWaitingModel(
            uuid=str(self.uuid),
            name='new',
            number=12345
        ).save()

    def tearDown(self):
        account_student.remove_fake_account()

    def testA_IDVerify(self):
        """
        TC about ID verification

        1. Check 'already existing ID'
        2. Check 'non-existing ID'
        """
        rv = self.client.post('/verify/id', data={'id': 'fake'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/verify/id', data={'id': 'doesntexist'})
        self.assertEqual(rv.status_code, 200)

    def testB_UUIDVerify(self):
        """
        TC about UUID verification

        1. Check 'already existing UUID'
        2. Check 'non-existing UUID'
        """
        rv = self.client.post('/verify/uuid', data={'uuid': str(u.uuid4())})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/verify/uuid', data={'uuid': str(self.uuid)})
        self.assertEqual(rv.status_code, 200)

    def testC_signup(self):
        """
        TC about student's signup

        1. Check 'UUID validation failed'
        2. Check 'ID validation failed'
        3. Check 'signup succeed'
        4. Check 'account_admin default data'
        """
        rv = self.client.post('/signup', data={'uuid': str(u.uuid4()), 'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 205)
        # UUID validation failed

        rv = self.client.post('/signup', data={'uuid': str(self.uuid), 'id': 'fake', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 204)
        # ID validation failed

        rv = self.client.post('/signup', data={'uuid': str(self.uuid), 'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 201)
        # Success

        access_token = account_student.get_access_token(self.client, 'doesntexist', 'fake')

        rv = self.client.get('/mypage', headers={'Authorization': access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue('name' in data)
        self.assertEqual(data['name'], 'new')
        self.assertTrue('number' in data)
        self.assertEqual(data['number'], 12345)

        account_student.remove_fake_account('doesntexist')
