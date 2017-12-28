import json
import unittest2 as unittest

from tests.views import account_student

from server import app


class TestAlteration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        account_student.create_fake_account()
        self.access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_student.remove_fake_account()

    def testA_changePW(self):
        """
        TC about password change

        1. Check 'unauthorized on password change'
        2. Check 'incorrect password'
        3. Check 'password change succeed'
        4. Check 'auth succeed'
        """
        rv = self.client.post('/change/pw')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/change/pw', headers={'Authorization': self.access_token}, data={'current_pw': 'invalid'})
        self.assertEqual(rv.status_code, 403)
        # Incorrect password

        rv = self.client.post('/change/pw', headers={'Authorization': self.access_token}, data={'current_pw': 'fake', 'new_pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Success

        rv = self.client.post('/auth', data={'id': 'fake_student', 'pw': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Auth check

    def testB_changeNumber(self):
        """
        TC about number change

        1. Check 'unauthorized on number change'
        2. Check 'number change succeed'
        3. Check 'changed number with /mypage'
        """
        rv = self.client.post('/change/number')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/change/number', data={'new_number': 2120}, headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        # Success

        rv = self.client.get('/mypage', headers={'Authorization': self.access_token})
        self.assertEqual(json.loads(rv.data.decode())['number'], 2120)
        # Number check
