import json
import unittest2 as unittest

from app.models.account import SignupWaitingModel
from tests.views import account_admin, account_student

from server import app


class TestAccountControl(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.access_token = account_admin.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_DeleteAccount(self):
        """
        TC about delete student account_admin control
    
        1. Check 'Authorization failed'
        2. Check 'Find number failed'
        3. Check 'delete success
        """
        rv = self.client.delete('/account_control', data={'number': 1234})
        self.assertEqual(rv.status_code, 401)
        # Authorization failed

        rv = self.client.delete('/account_control', headers={'Authorization': self.access_token}, data={'number': 0000})
        self.assertEqual(rv.status_code, 204)
        # Find number failed

        rv = self.client.delete('/account_control', headers={'Authorization': self.access_token}, data={'number': 1234})
        self.assertEqual(rv.status_code, 200)
        # Success

    def testB_FindUUID(self):
        """
        TC about find uuid in SignupWationgModel
        1. Check 'Authorization failed'
        2. Check 'Find number failed'
        3. Check 'Success'
        """
        self.client.delete('/account_control', headers={'Authorization': self.access_token}, data={'number': 1234})
        rv = self.client.get('/account_control', data={'number': 1234})
        self.assertEqual(rv.status_code, 401)
        # Authorization failed

        rv = self.client.get('/account_control', headers={'Authorization': self.access_token}, data={'number': 0000})
        self.assertEqual(rv.status_code, 204)
        # Find number failed

        rv = self.client.get('/account_control', headers={'Authorization': self.access_token}, data={'number': 1234})
        self.assertEqual(rv.status_code, 200)
        uuid = SignupWaitingModel.objects(number=1234).first().uuid
        response = json.loads(rv.data.decode())
        self.assertEqual(uuid, response['uuid'])
        # Success
