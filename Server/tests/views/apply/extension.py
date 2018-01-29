import json
import unittest

from tests.views import account_admin, account_student

from server import app


class TestExtension(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_applyExtension11(self):
        """
        TC about 11:00's extension apply

        - Preparations
        Check apply data is empty

        - Exception Tests
        Forbidden with admin access token

        - Process
        Apply

        - Validation
        Check apply data is existing
        """
        # -- Preparations --
        rv = self.client.get('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/extension/11', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/extension/11', headers={'Authorization': self.student_access_token}, data={'class_num': 1, 'seat_num': 21})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(data['class_num'], 1)
        self.assertEqual(data['seat_num'], 21)
        # -- Validation --

    def testB_withdrawExtension11(self):
        """
        TC about 11:00's extension withdraw

        - Preparations
        Apply sample data

        - Exception Tests
        Forbidden with admin access token

        - Process
        Withdraw

        - Validation
        Check apply data is empty
        """
        # -- Preparations --
        self.client.post('/extension/11', headers={'Authorization': self.student_access_token}, data={'class_num': 1, 'seat_num': 21})
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.delete('/extension/11', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.delete('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Validation --

    def testC_applyExtension12(self):
        """
        TC about 12:00's extension apply

        - Preparations
        Check apply data is empty

        - Exception Tests
        Forbidden with admin access token

        - Process
        Apply

        - Validation
        Check apply data is existing
        """
        # -- Preparations --
        rv = self.client.get('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/extension/12', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/extension/12', headers={'Authorization': self.student_access_token}, data={'class_num': 1, 'seat_num': 21})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(data['class_num'], 1)
        self.assertEqual(data['seat_num'], 21)
        # -- Validation --

    def testD_withdrawExtension12(self):
        """
        TC about 12:00's extension withdraw

        - Preparations
        Apply sample data

        - Exception Tests
        Forbidden with admin access token

        - Process
        Withdraw

        - Validation
        Check apply data is empty
        """
        # -- Preparations --
        self.client.post('/extension/12', headers={'Authorization': self.student_access_token}, data={'class_num': 1, 'seat_num': 21})
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.delete('/extension/12', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.delete('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Validation --

    def testE_downloadExtension11(self):
        """
        TC about 11:00's extension data download

        - Preparations
        Apply sample data

        - Exception Tests
        Forbidden with student access token

        - Process
        Download excel file

        - Validation
        * Validation required
        """
        # -- Preparations --
        self.client.post('/extension/11', headers={'Authorization': self.student_access_token}, data={'class_num': 1, 'seat_num': 21})
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/admin/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        self.client.get('/admin/extension/11', headers={'Authorization': self.admin_access_token})
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testF_downloadExtension12(self):
        """
        TC about 12:00's extension data download

        - Preparations
        Apply sample data

        - Exception Tests
        Forbidden with student access token

        - Process
        Download excel file

        - Validation
        * Validation required
        """
        # -- Preparations --
        self.client.post('/extension/12', headers={'Authorization': self.student_access_token}, data={'class_num': 1, 'seat_num': 21})
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/admin/extension/12', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        self.client.get('/admin/extension/12', headers={'Authorization': self.admin_access_token})
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testG_loadExtensionMap(self):
        """
        TC about extension data map loading

        - Preparations
        None

        - Exception Tests
        None

        - Process
        Load map

        - Validation
        Check length of loaded list
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/extension/map/11', query_string={'class_num': 1})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(len(json.loads(rv.data.decode())), 5)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/extension/map/12', query_string={'class_num': 1})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(len(json.loads(rv.data.decode())), 5)
        # -- Validation --
