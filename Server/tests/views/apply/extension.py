from datetime import datetime
import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app
from utils.extension_meta import *


class TestExtension(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_applyExtension11(self):
        """
        TC about extension apply 11

        1. Check 'unapplied'
        2. Check 'apply succeed'
        3. Check 'apply status'
        """
        rv = self.client.get('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

        rv = self.client.post('/extension/11', headers={'Authorization': self.student_access_token}, data={'class': 1, 'seat': 21})
        if APPLY_START < datetime.now().time() < APPLY_END_11:
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/extension/11', headers={'Authorization': self.student_access_token})
            self.assertEqual(rv.status_code, 200)

            data = json.loads(rv.data.decode())
            self.assertEqual(data['class'], 1)
            self.assertEqual(data['seat'], 21)
        else:
            self.assertEqual(rv.status_code, 204)

    def testB_withdrawExtension11(self):
        """
        TC about withdraw extension apply 11

        1. Check 'withdraw succeed'
        2. Check 'unapplied'
        """
        rv = self.client.delete('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # Withdraw success

        rv = self.client.get('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

    def testC_applyExtension12(self):
        """
        TC about extension apply 12

        1. Check 'unapplied'
        2. Check 'apply succeed'
        3. Check 'apply status'
        """
        rv = self.client.get('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

        rv = self.client.post('/extension/12', headers={'Authorization': self.student_access_token}, data={'class': 1, 'seat': 21})
        if APPLY_START < datetime.now().time() < APPLY_END_12:
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/extension/12', headers={'Authorization': self.student_access_token})
            self.assertEqual(rv.status_code, 200)

            data = json.loads(rv.data.decode())
            self.assertEqual(data['class'], 1)
            self.assertEqual(data['seat'], 21)
        else:
            self.assertEqual(rv.status_code, 204)

    def testD_withdrawExtension12(self):
        """
        TC about withdraw extension apply 12

        1. Check 'withdraw succeed'
        2. Check 'unapplied'
        """
        rv = self.client.delete('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # Withdraw success

        rv = self.client.get('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # Unapplied check

    def testE_downloadExtension11(self):
        """
        TC about download extension apply 11
        """
        rv = self.client.get('/admin/extension/11', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)

    def testF_downloadExtension12(self):
        """
        TC about download extension apply 12
        """
        rv = self.client.get('/admin/extension/12', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
