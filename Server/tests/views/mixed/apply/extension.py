from datetime import datetime
import json
import unittest2 as unittest

from tests.views import student

from server import app
from utils.extension_meta import *


class TestExtension(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        student.create_fake_account()
        self.access_token = student.get_access_token(self.client)

    def tearDown(self):
        student.remove_fake_account()

    def testExtension11(self):
        rv = self.client.get('/extension/11', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/extension/11')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/extension/11', headers={'Authorization': self.access_token}, data={'class': 1, 'seat': 21})
        if APPLY_START < datetime.now().time() < APPLY_END_11:
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/extension/11', headers={'Authorization': self.access_token})
            self.assertEqual(rv.status_code, 200)

            data = json.loads(rv.data.decode())
            self.assertEqual(data['class'], 1)
            self.assertEqual(data['seat'], 10)
        else:
            self.assertEqual(rv.status_code, 204)

    def testExtension12(self):
        rv = self.client.get('/extension/12', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/extension/12')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/extension/12', headers={'Authorization': self.access_token}, data={'class': 1, 'seat': 21})
        if APPLY_START < datetime.now().time() < APPLY_END_12:
            self.assertEqual(rv.status_code, 201)
            # Apply success

            rv = self.client.get('/extension/12', headers={'Authorization': self.access_token})
            self.assertEqual(rv.status_code, 200)

            data = json.loads(rv.data.decode())
            self.assertEqual(data['class'], 1)
            self.assertEqual(data['seat'], 10)
        else:
            self.assertEqual(rv.status_code, 204)
