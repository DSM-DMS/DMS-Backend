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

    def testA_mypage(self):
        """
        TC about mypage

        1. Check 'unauthorized on inquire mypage'
        2. Check 'mypage data'
        """
        rv = self.client.get('/mypage')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        access_token = account_student.get_access_token(self.client)

        rv = self.client.get('/mypage', headers={'Authorization': access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue('name' in data)
        self.assertEqual(data['name'], 'fake')
        self.assertTrue('number' in data)
        self.assertEqual(data['number'], 1234)

        self.assertTrue('extension_11' in data)
        self.assertEqual(data['extension_11'], None)
        self.assertTrue('extension_12' in data)
        self.assertEqual(data['extension_12'], None)

        self.assertTrue('goingout' in data)
        self.assertEqual(data['goingout']['sat'], False)
        self.assertEqual(data['goingout']['sun'], False)

        self.assertEqual(data['stay_value'], 4)