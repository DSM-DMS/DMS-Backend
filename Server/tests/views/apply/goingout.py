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

        - Preparations
        Check apply data is all False

        - Exception Tests
        Forbidden with admin access token

        - Process
        Apply

        - Validation
        Check apply data
        """
        # -- Preparations --
        rv = self.client.get('/goingout', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertFalse(all((data['sat'], data['sun'])))
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/goingout', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/goingout', headers={'Authorization': self.student_access_token}, data={'sat': True, 'sun': False})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/goingout', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue(data['sat'])
        self.assertFalse(data['sun'])
        # -- Validation --

    def testB_download(self):
        """
        TC about goingout data download

        - Preparations
        None

        - Exception Tests
        Forbidden with student access token

        - Process
        Download excel file
        Download with another apply values

        - Validation
        * Validation required
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/admin/goingout', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        self.client.get('/admin/goingout', headers={'Authorization': self.admin_access_token})

        rv = self.client.post('/goingout', headers={'Authorization': self.student_access_token}, data={'sat': True, 'sun': False})
        self.assertEqual(rv.status_code, 201)
        self.client.get('/admin/goingout', headers={'Authorization': self.admin_access_token})

        rv = self.client.post('/goingout', headers={'Authorization': self.student_access_token}, data={'sat': False, 'sun': True})
        self.assertEqual(rv.status_code, 201)
        self.client.get('/admin/goingout', headers={'Authorization': self.admin_access_token})

        rv = self.client.post('/goingout', headers={'Authorization': self.student_access_token}, data={'sat': True, 'sun': True})
        self.assertEqual(rv.status_code, 201)
        self.client.get('/admin/goingout', headers={'Authorization': self.admin_access_token})
        # -- Process --

        # -- Validation --
        # -- Validation --
