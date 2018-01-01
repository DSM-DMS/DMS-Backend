from datetime import datetime, time
import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestStay(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_apply(self):
        """
        TC about stay apply

        1. Check 'applied value 4'
        2. Check 'apply succeed'
        3. Check 'apply status'
        """
        rv = self.client.get('/stay', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.data.decode())['value'], 4)

        rv = self.client.post('/stay', headers={'Authorization': self.student_access_token}, data={'value': 1})
        now = datetime.now()
        if (now.weekday() == 6 and now.time() > time(20, 30)) or (0 < now.weekday() < 3) or (now.weekday() == 3 and now.time() < time(22, 00)):
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/stay', headers={'Authorization': self.student_access_token})
            self.assertEqual(rv.status_code, 200)

            self.assertEqual(json.loads(rv.data.decode())['value'], 1)
        else:
            self.assertEqual(rv.status_code, 204)

    def testB_download(self):
        """
        TC about download stay apply
        """
        rv = self.client.get('/admin/stay', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
