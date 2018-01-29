import json
import unittest

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

        - Preparations
        Check apply data is 4

        - Exception Tests
        Forbidden with admin access token

        - Process
        Apply

        - Validation
        Check apply data
        """
        # -- Preparations --
        rv = self.client.get('/stay', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.data.decode())['value'], 4)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/stay', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/stay', headers={'Authorization': self.student_access_token}, data={'value': 1})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/stay', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)

        self.assertEqual(json.loads(rv.data.decode())['value'], 1)
        # -- Validation --

    def testB_download(self):
        """
        TC about stay data download

        - Preparations
        Apply sample data

        - Exception Tests
        Forbidden with student access token

        - Process
        Download excel file
        Download with another apply values

        - Validation
        * Validation required
        """
        # -- Preparations --
        rv = self.client.post('/stay', headers={'Authorization': self.student_access_token}, data={'value': 1})
        self.assertEqual(rv.status_code, 201)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/admin/stay', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        self.client.get('/admin/stay', headers={'Authorization': self.admin_access_token})

        rv = self.client.post('/stay', headers={'Authorization': self.student_access_token}, data={'value': 2})
        self.assertEqual(rv.status_code, 201)
        self.client.get('/admin/stay', headers={'Authorization': self.admin_access_token})

        rv = self.client.post('/stay', headers={'Authorization': self.student_access_token}, data={'value': 3})
        self.assertEqual(rv.status_code, 201)
        self.client.get('/admin/stay', headers={'Authorization': self.admin_access_token})

        rv = self.client.post('/stay', headers={'Authorization': self.student_access_token}, data={'value': 4})
        self.assertEqual(rv.status_code, 201)
        self.client.get('/admin/stay', headers={'Authorization': self.admin_access_token})
        # -- Process --

        # -- Validation --
        # -- Validation --
