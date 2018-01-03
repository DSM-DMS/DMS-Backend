import json
import unittest2 as unittest
import uuid as u

from app.models.account import SignupWaitingModel
from tests.views import account_student

from server import app


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_student.create_fake_account()
        self.uuid = u.uuid4()

        SignupWaitingModel(
            uuid=str(self.uuid),
            name='new',
            number=1111
        ).save()

    def tearDown(self):
        account_student.remove_fake_account()
        account_student.remove_fake_account('doesntexist')

    def testA_verifyID(self):
        """
        TC about ID verification

        - Preparations
        None

        - Exception Tests
        Non-existing ID

        - Process
        Verify ID

        - Validation
        None
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/verify/id', data={'id': 'fake_student'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/verify/id', data={'id': 'doesntexist'})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testB_verifyUUID(self):
        """
        TC about UUID verification

        - Preparations
        None

        - Exception Tests
        Non-existing UUID

        - Process
        Verify UUID

        - Validation
        None
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/verify/uuid', data={'uuid': str(u.uuid4())})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/verify/uuid', data={'uuid': str(self.uuid)})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testC_signup(self):
        """
        TC about Signup

        - Preparations
        None

        - Exception Tests
        Non-existing UUID
        Already existing ID

        - Process
        Signup

        - Validation
        Auth with signed ID/PW
        Check student data
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/signup', data={'uuid': str(u.uuid4()), 'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 205)

        rv = self.client.post('/signup', data={'uuid': str(self.uuid), 'id': 'fake_student', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/signup', data={'uuid': str(self.uuid), 'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.post('/auth', data={'id': 'doesntexist', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data and 'refresh_token' in data)
        access_token = 'JWT ' + data['access_token']

        rv = self.client.get('/mypage', headers={'Authorization': access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(data['name'], 'new')
        self.assertEqual(data['number'], 1111)
        # -- Validation --
