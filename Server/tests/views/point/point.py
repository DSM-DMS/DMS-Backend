import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from app.models.point import PointRuleModel
from server import app


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()

        self.access_token = account_admin.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()
        PointRuleModel.objects.delete()

    def testA_insertPointData(self):
        """
        TC about student point data initialization

        - Preparations
        Check existing student data

        - Exception Tests
        None

        - Process
        Initialize student point with sample data

        - Validation
        Check inserted student point data
        """
        # -- Preparations --
        rv = self.client.get('/admin/managing/student', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())[0]
        self.assertTrue(not all((data['good_point'], data['bad_point'], data['penalty_training_status'])))
        # All None
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/managing/student', headers={'Authorization': self.access_token}, data={
            'id': 'fake_student',
            'good_point': 1,
            'bad_point': 2,
            'penalty_training_status': 0
        })
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/admin/managing/student', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())[0]
        self.assertTrue(all((data['good_point'], data['bad_point'], data['penalty_training_status'] == 0)))
        # -- Validation --

    def testB_insertPointRule(self):
        """
        TC about point rule insertion

        - Preparations
        Check existing rule list is empty

        - Exception Tests
        None

        - Process
        Insert rule data

        - Validation
        Check inserted rule data
        """
        # -- Preparations --
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertFalse(json.loads(rv.data.decode()))
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/managing/rule', headers={'Authorization': self.access_token}, data={
            'name': 'test',
            'min_point': 1,
            'max_point': 1
        })
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.data.decode())[0]['name'], 'test')
        # -- Validation --

    def testC_patchPointRule(self):
        """
        TC about point rule modification

        - Preparations
        Add sample rule data and take rule ID

        - Exception Tests
        Non-existing rule ID
        Short rule ID

        - Process
        Modify point rule

        - Validation
        Check modified rule data
        """
        # -- Preparations --
        self.client.post('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'name': 'test', 'min_point': 1, 'max_point': 1})
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        rule_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.patch('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'rule_id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.patch('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'rule_id': '1234'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.patch('/admin/managing/rule', headers={'Authorization': self.access_token}, data={
            'rule_id': rule_id,
            'name': 'new',
            'min_point': 2,
            'max_point': 2
        })
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())[0]
        self.assertTrue(data['name'] == 'new' and data['min_point'] == data['max_point'] == 2)
        # -- Validation --

    def testD_deleteRule(self):
        """
        TC about

        - Preparations
        Add sample rule data and take rule ID

        - Exception Tests
        Non-existing rule ID
        Short rule ID

        - Process
        Delete rule

        - Validation
        Check rule list is empty
        """
        # -- Preparations --
        self.client.post('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'name': 'test', 'min_point': 1, 'max_point': 1})
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        rule_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.delete('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'rule_id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.delete('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'rule_id': '1234'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.delete('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'rule_id': rule_id})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertFalse(json.loads(rv.data.decode()))
        # -- Validation --

    def testE_givePoint(self):
        """
        TC about point giving

        - Preparations
        Add sample student point data
        Add sample rule data and take rule ID

        - Exception Tests
        Non-existing student ID
        Non-existing rule ID
        Short rule ID

        - Process
        Give point to student

        - Validation
        Check sample student's point history
        """
        # -- Preparations --
        self.client.post('/admin/managing/student', headers={'Authorization': self.access_token}, data={
            'id': 'fake_student',
            'good_point': 1,
            'bad_point': 2,
            'penalty_training_status': 0
        })

        self.client.post('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'name': 'test', 'min_point': 1, 'max_point': 1})
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        rule_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/managing/point', headers={'Authorization': self.access_token}, data={'id': 'doesntexist'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/admin/managing/point', headers={'Authorization': self.access_token}, data={'id': 'fake_student', 'rule_id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 205)

        rv = self.client.post('/admin/managing/point', headers={'Authorization': self.access_token}, data={'id': 'fake_student', 'rule_id': '1234'})
        self.assertEqual(rv.status_code, 205)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/managing/point', headers={'Authorization': self.access_token}, data={
            'id': 'fake_student',
            'rule_id': rule_id,
            'point': 1
        })
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/admin/managing/point', headers={'Authorization': self.access_token}, query_string={'id': 'fake_student'})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(len(data), 1)
        self.assertTrue(data[0]['reason'] == 'test' and data[0]['point'] == 1)
        # -- Validation --
