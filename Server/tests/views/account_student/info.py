import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestInfo(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_getMypage(self):
        """
        TC about mypage loading

        - Preparations
        None

        - Exception Tests
        Forbidden with admin access token

        - Process
        Load mypage(student info)

        - Validation
        Check student data
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/mypage', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/mypage', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        data = json.loads(rv.data.decode())
        self.assertEqual(data['name'], 'fake')
        self.assertEqual(data['number'], 1111)

        self.assertEqual(data['extension_11'], None)
        self.assertEqual(data['extension_12'], None)
        self.assertEqual(data['goingout']['sat'], False)
        self.assertEqual(data['goingout']['sun'], False)
        self.assertEqual(data['stay_value'], 4)
        # -- Validation --
