from datetime import datetime
import json
import unittest2 as unittest

from tests.views import account_student

from server import app
from utils.extension_meta import *


class TestExtension(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_student.create_fake_account()
        self.access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_student.remove_fake_account()

    def testA_extension11Apply(self):
        """
        TC about extension apply 11

        1. Check 'unapplied'
        2. Check 'unauthorized on extension apply'
        3. Check 'apply succeed'
        4. Check 'apply status'
        """
        rv = self.client.get('/extension/11', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

        rv = self.client.post('/extension/11')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/extension/11', headers={'Authorization': self.access_token}, data={'class': 1, 'seat': 21})
        if APPLY_START < datetime.now().time() < APPLY_END_11:
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/extension/11', headers={'Authorization': self.access_token})
            self.assertEqual(rv.status_code, 200)

            data = json.loads(rv.data.decode())
            self.assertEqual(data['class'], 1)
            self.assertEqual(data['seat'], 21)
        else:
            self.assertEqual(rv.status_code, 204)

    def testB_extension11Withdraw(self):
        """
        TC about withdraw extension apply 11

        1. Check 'unauthorized on withdraw'
        2. Check 'withdraw succeed'
        3. Check 'unapplied'
        """
        rv = self.client.delete('/extension/11')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.delete('/extension/11', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        # Withdraw success

        rv = self.client.get('/extension/11', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

    def testC_extension12Apply(self):
        """
        TC about extension apply 12

        1. Check 'unapplied'
        2. Check 'unauthorized on extension apply'
        3. Check 'apply succeed'
        4. Check 'apply status'
        """
        rv = self.client.get('/extension/12', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

        rv = self.client.post('/extension/12')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/extension/12', headers={'Authorization': self.access_token}, data={'class': 1, 'seat': 21})
        if APPLY_START < datetime.now().time() < APPLY_END_12:
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/extension/12', headers={'Authorization': self.access_token})
            self.assertEqual(rv.status_code, 200)

            data = json.loads(rv.data.decode())
            self.assertEqual(data['class'], 1)
            self.assertEqual(data['seat'], 21)
        else:
            self.assertEqual(rv.status_code, 204)

    def testD_extension12Withdraw(self):
        """
        TC about withdraw extension apply 12

        1. Check 'unauthorized on withdraw'
        2. Check 'withdraw succeed'
        3. Check 'unapplied'
        """
        rv = self.client.delete('/extension/12')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.delete('/extension/12', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        # Withdraw success

        rv = self.client.get('/extension/12', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

    def testE_extension11Download(self):
        pass

    def testF_extension12Download(self):
        pass
