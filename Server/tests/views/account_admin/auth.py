import json
import unittest2 as unittest

from tests.views import account_admin

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()

    def tearDown(self):
        account_admin.remove_fake_account()

    def testA_auth(self):
        """
        TC about admin authentication

        - Preparations
        None

        - Exception Tests
        Incorrect ID or PW

        - Process
        Auth

        - Validation
        Check access token, refresh token
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/auth', data={'id': 'fake_admin', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data and 'refresh_token' in data)
        # -- Validation --

    def testB_refresh(self):
        """
        TC about admin account refresh

        - Preparations
        None

        - Exception Tests
        None

        - Process
        Refresh account

        - Validation
        Check refresh token
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        refresh_token = account_admin.get_refresh_token(self.client)
        rv = self.client.post('/admin/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        self.assertTrue('access_token' in json.loads(rv.data.decode()))
        # -- Validation --
