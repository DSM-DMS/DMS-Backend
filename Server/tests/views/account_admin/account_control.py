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

    def testA_deleteAccount(self):
        """
        TC about student account deletion
    
        1. Check 'Authorization failed'
        2. Check 'Find number failed'
        3. Check 'Delete and get uuid succeed'
        """
        rv = self.client.post('/admin/account-control', data={'number': 1234})
        self.assertEqual(rv.status_code, 401)
        # Authorization failed

        rv = self.client.post('/admin/account-control', headers={'Authorization': self.access_token}, data={'number': 0000})
        self.assertEqual(rv.status_code, 204)
        # Find number failed

        rv = self.client.post('/admin/account-control', headers={'Authorization': self.access_token}, data={'number': 0000})
        self.assertEqual(rv.status_code, 201)
        # Delete and get uuid Success

    def testB_findUUID(self):
        """
        TC about find uuid via student number

        1. Initialize account
        2. Check 'Succeed'
        """
        self.client.post('/admin/account-control', headers={'Authorization': self.access_token}, data={'number': 1234})
        # Initialize account

        rv = self.client.post('/admin/account-control', headers={'Authorization': self.access_token}, data={'number': 1234})
        self.assertEqual(rv.status_code, 201)
        # Succeed

        uuid = SignupWaitingModel.objects(number=1234).first().uuid
        response = json.loads(rv.data.decode())
        self.assertEqual(uuid, response['uuid'])
        # Validate
