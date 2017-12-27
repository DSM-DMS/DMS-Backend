import json
import unittest2 as unittest

from tests.views import account_student

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        account_student.create_fake_account()

    def tearDown(self):
        account_student.remove_fake_account()

    def testA_auth(self):
        """
        TC about student's auth

        1. Check 'login failed'
        2. Check 'login succeed'
        3. Check 'access token/refresh token'
        """
        rv = self.client.post('/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # Login fail

        rv = self.client.post('/auth', data={'id': 'fake', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 200)
        # Success

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data and 'refresh_token' in data)
        # Token check

    def testB_refresh(self):
        """
        TC about admin's refresh

        1. Check 'unauthorized on refresh'
        2. Check 'refresh success'
        3. Check 'new access token'
        4. Check 'refresh failed after password changed'
        """
        rv = self.client.post('/refresh')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        refresh_token = account_student.get_refresh_token(self.client)
        rv = self.client.post('/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 200)
        # Success

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data)
        # New access token check

        access_token = account_student.get_access_token(self.client)
        rv = self.client.post('/change/pw', headers={'Authorization': access_token}, data={'current_pw': 'fake', 'new_pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Change password

        rv = self.client.post('/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 205)
        # Refresh fail after password changed
