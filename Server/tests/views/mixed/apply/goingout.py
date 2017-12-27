import json
import unittest2 as unittest

from tests.views import student

from server import app


class TestGoingout(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        student.create_fake_account()
        self.access_token = student.get_access_token(self.client)

    def tearDown(self):
        student.remove_fake_account()

    def testGoingout(self):
        rv = self.client.get('/goingout', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(data['sat'], False)
        self.assertEqual(data['sun'], False)

        rv = self.client.post('/goingout')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/goingout', headers={'Authorization': self.access_token}, data={'sat': True, 'sun': False})
        self.assertEqual(rv.status_code, 201)
        # Apply success

        rv = self.client.get('/goingout', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(data['sat'], True)
        self.assertEqual(data['sun'], False)
