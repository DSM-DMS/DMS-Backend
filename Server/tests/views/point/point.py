import json
import unittest2 as unittest

from tests.views import account_admin, account_student

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

    def testA_insertPointData(self):
        """
        TC about student point data inserting
        """
        rv = self.client.get('/admin/managing/student', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())

        flag = False
        for student in data:
            if student['id'] == 'fake_student' and student['good_point'] == student['bad_point'] == student['penalty_training_status'] == None:
                flag = True

        self.assertTrue(flag)
        # Existing student data

        rv = self.client.post('/admin/managing/student', headers={'Authorization': self.access_token}, data={'id': 'fake_student', 'good_point': 1, 'bad_point': 2, 'penalty_training_status': 0})
        self.assertEqual(rv.status_code, 201)
        # Success

        rv = self.client.get('/admin/managing/student', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())

        flag = False
        for student in data:
            if student['id'] == 'fake_student' and student['good_point'] == 1 and student['bad_point'] == 2 and student['penalty_training_status'] == 0:
                flag = True

        self.assertTrue(flag)

    def testB_insertPointRule(self):
        """
        TC about point rule inserting
        """
        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())
        self.assertEqual(type(data), list)
        # Existing data

        rv = self.client.post('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'name': 'test', 'min_point': 1, 'max_point': 1})
        self.assertEqual(rv.status_code, 201)
        # Success

        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())

        flag = False
        for rule in data:
            if rule['name'] == 'test' and rule['min_point'] == rule['max_point'] == 1:
                flag = True

        self.assertTrue(flag)

    def testC_patchPointRule(self):
        """
        TC about point rule patching
        """
        rv = self.client.post('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'name': 'test', 'min_point': 1, 'max_point': 1})
        self.assertEqual(rv.status_code, 201)
        # Add rule

        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())

        rule_id = ''
        for rule in data:
            if rule['name'] == 'test' and rule['min_point'] == rule['max_point'] == 1:
                rule_id = rule['id']

        rv = self.client.patch('/admin/managing/rule', headers={'Authorization': self.access_token}, data={'rule_id': rule_id, 'name': 'new', 'min_point': 2, 'max_point': 2})
        self.assertEqual(rv.status_code, 200)
        # Success

        rv = self.client.get('/admin/managing/rule', headers={'Authorization': self.access_token})
        self.assertEqual(rv.status_code, 200)
        data = json.loads(rv.data.decode())

        flag = False
        for rule in data:
            if rule['name'] == 'new' and rule['min_point'] == rule['max_point'] == 2:
                flag = True

        self.assertTrue(flag)

    def testD_givePoint(self):
        """
        TC about student point giving
        """

    def testE_deleteRule(self):
        """
        TC about point rule deletion
        """
