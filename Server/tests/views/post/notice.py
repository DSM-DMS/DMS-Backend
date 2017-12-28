import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestNotice(unittest.TestCase):
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
        TC about notice upload

        1. Check 'unauthorized on notice upload'
        2. Check 'upload succeed'
        """
        rv = self.client.post('/admin/notice')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post success

    def testB_get(self):
        """
        TC about notice get
        """

    def testC_patch(self):
        """
        TC about notice patch

        1. Check 'unauthorized on notice getting'
        2. Load/Check 'existing(uploaded) notice'
        3. Check 'unauthorized on notice patch'
        4. Check 'patch succeed'
        """
        rv = self.client.get('/notice')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.get('/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get success

        data = json.loads(rv.data.decode())

        post_id = ''
        for notice in data:
            if notice['title'] == 'test' and notice['author'] == 'fake':
                post_id = notice['id']

        self.assertTrue(post_id)
        # Data validate

        rv = self.client.patch('/admin/notice')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.patch('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.patch('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'id': post_id, 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Patch success

    def testD_delete(self):
        """
        TC about notice delete

        1. Check 'unauthorized on notice getting'
        2. Load/Check 'existing(uploaded) notice'
        3. Check 'unauthorized on notice delete'
        4. Check 'delete succeed'
        """
        rv = self.client.get('/notice')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.get('/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get success

        data = json.loads(rv.data.decode())

        post_id = ''
        for notice in data:
            if notice['title'] == 'new' and notice['author'] == 'fake':
                post_id = notice['id']

        self.assertTrue(post_id)
        # Data validate

        rv = self.client.delete('/admin/notice')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.delete('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.delete('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 200)
        # Delete success
