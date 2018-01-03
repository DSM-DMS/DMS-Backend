import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from app.models.post import RuleModel
from server import app


class TestRule(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()
        RuleModel.objects.delete()

    def testA_post(self):
        """
        TC about rule uploading

        - Preparations
        None

        - Exception Tests
        Forbidden with student access token

        - Process
        Post rule data

        - Validation
        Check post data is existing
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode()))
        # -- Validation --

    def testB_get(self):
        """
        TC about rule data getting

        - Preparations
        Post sample rule data
        Take rule ID

        - Exception Tests
        Short rule ID with admin/student access token
        Non-existing rule ID with admin/student access token

        - Process
        Load rule data with admin access token
        Load rule data with student access token

        - Validation
        None
        """
        # -- Preparations --
        rv = self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/rule/1234', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.get('/rule/1234', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.get('/rule/123456789012345678901234', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.get('/rule/123456789012345678901234', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        rule_id = json.loads(rv.data.decode())[0]['id']

        rv = self.client.get('/rule/' + rule_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode()))

        rv = self.client.get('/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        rule_id = json.loads(rv.data.decode())[0]['id']

        rv = self.client.get('/rule/' + rule_id, headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode()))
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testC_patch(self):
        """
        TC about rule data patching

        - Preparations
        Post sample rule data
        Take rule ID

        - Exception Tests
        Forbidden with student access token
        Short rule ID
        Non-existing rule ID

        - Process
        Change rule data

        - Validation
        Check changed rule data
        """
        # -- Preparations --
        rv = self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)

        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        rule_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.patch('/admin/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.patch('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': '1234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.patch('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.patch('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': rule_id, 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/rule/' + rule_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'new')
        # -- Validation --

    def testD_delete(self):
        """
        TC about rule data deletion

        - Preparations
        Post sample rule data
        Take rule ID

        - Exception Tests
        Forbidden with student access token
        Short rule ID
        Non-existing rule ID

        - Process
        Delete rule data

        - Validation
        Check rule data is empty
        """
        # -- Preparations --
        rv = self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)

        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        rule_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.delete('/admin/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.delete('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': '1234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.delete('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.delete('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': rule_id})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/rule/' + rule_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Validation --
