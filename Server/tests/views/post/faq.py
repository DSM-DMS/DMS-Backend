import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestFAQ(unittest.TestCase):
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
        TC about FAQ upload

        1. Check 'upload succeed'
        """
        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post success

    def testB_get(self):
        """
        TC about FAQ get
        1. Check short wrong id
        2. Check wrong id
        3. Success
        """
        self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})

        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        rule_id = json.loads(rv.data.decode())[0]['id']
        # Make rule and get rule id

        rv = self.client.get('/faq/1234', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)
        # Check short wrong id

        rv = self.client.get('/faq/123456789012345678901234', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)
        # Check wrong id

        rv = self.client.get('/faq/'+rule_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Success

    def testC_patch(self):
        """
        TC about FAQ patch

        1. Load/Check 'existing(uploaded) FAQ'
        2. Check 'unauthorized on FAQ patch'
        3. Check 'patch succeed'
        """
        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get success

        data = json.loads(rv.data.decode())

        post_id = ''
        for faq in data:
            if faq['title'] == 'test' and faq['author'] == 'fake':
                post_id = faq['id']

        self.assertTrue(post_id)
        # Data validate

        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': post_id, 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Patch success

    def testD_delete(self):
        """
        TC about FAQ delete

        1. Load/Check 'existing(uploaded) FAQ'
        2. Check 'delete succeed'
        """
        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get success

        data = json.loads(rv.data.decode())

        post_id = ''
        for faq in data:
            if faq['title'] == 'new' and faq['author'] == 'fake':
                post_id = faq['id']

        self.assertTrue(post_id)
        # Data validate

        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 200)
        # Delete success
