import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestAlteration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_student.remove_fake_account()

    def testA_changePW(self):
        """
        TC about password changing

        - Preparations
        None

        - Exception Tests
        Incorrect current password

        - Process
        Change password

        - Validation
        Auth with changed password
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/change/pw', headers={'Authorization': self.student_access_token}, data={'current_pw': 'invalid'})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/change/pw', headers={'Authorization': self.student_access_token}, data={'current_pw': 'fake', 'new_pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.post('/auth', data={'id': 'fake_student', 'pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # -- Validation --

    def testB_changeNumber(self):
        """
        TC about number changing

        - Preparations
        None

        - Exception Tests
        Forbidden with admin access token

        - Process
        Change number

        - Validation
        Check changed student number
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/change/number', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/change/number', headers={'Authorization': self.student_access_token}, data={'new_number': 2120})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/mypage', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.data.decode())['number'], 2120)
        # -- Validation --
