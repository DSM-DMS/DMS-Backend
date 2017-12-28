import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestRule(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()

        self.admin_access_token = account_admin.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_post(self):
        """
        TC about rule upload

        1. Check 'upload succeed'
        """
        rv = self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post success

    def testB_get(self):
        """
        TC about rule get
        """

    def testC_patch(self):
        """
        TC about rule patch

        1. Load/Check 'existing(uploaded) rule'
        2. Check 'patch succeed'
        """
        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get success

        data = json.loads(rv.data.decode())

        post_id = ''
        for rule in data:
            if rule['title'] == 'test' and rule['author'] == 'fake':
                post_id = rule['id']

        self.assertTrue(post_id)
        # Data validate

        rv = self.client.patch('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.patch('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': post_id, 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Patch success

    def testD_delete(self):
        """
        TC about rule delete

        1. Load/Check 'existing(uploaded) rule'
        2. Check 'delete succeed'
        """
        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get success

        data = json.loads(rv.data.decode())

        post_id = ''
        for rule in data:
            if rule['title'] == 'new' and rule['author'] == 'fake':
                post_id = rule['id']

        self.assertTrue(post_id)
        # Data validate

        rv = self.client.delete('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.delete('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 200)
        # Delete success
