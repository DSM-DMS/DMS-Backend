import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestGoingout(unittest.TestCase):
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
        TC about goingout apply

        1. Check 'apply status all false'
        2. Check 'apply succeed'
        3. Check 'apply status'
        """
        rv = self.client.get('/goingout', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())
        self.assertFalse(all((data['sat'], data['sun'])))

        rv = self.client.post('/goingout', headers={'Authorization': self.student_access_token}, data={'sat': True, 'sun': False})
        self.assertEqual(rv.status_code, 201)
        # Apply success

        rv = self.client.get('/goingout', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())
        self.assertEqual(data['sat'], True)
        self.assertEqual(data['sun'], False)

    def testB_download(self):
        """
        TC about download goingout apply
        """
        self.client.post('/goingout', headers={'Authorization': self.student_access_token}, data={'sat': True, 'sun': False})
        # Sample data

        rv = self.client.get('/admin/goingout', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
