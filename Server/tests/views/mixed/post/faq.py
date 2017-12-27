import json
import unittest2 as unittest

from tests.views import admin, student

from server import app


class TestFAQ(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        admin.create_fake_account()
        student.create_fake_account()

        self.admin_access_token = admin.get_access_token(self.client)

    def tearDown(self):
        student.remove_fake_account()
        admin.remove_fake_account()

    def testA_post(self):
        """
        TC about FAQ upload

        1. Check 'unauthorized on FAQ upload'
        2. Check 'upload succeed'
        """
        rv = self.client.post('/admin/faq')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post success

    def testB_get(self):
        """
        TC about FAQ get
        """

    def testC_patch(self):
        """
        TC about FAQ patch

        1. Check 'unauthorized on FAQ getting'
        2. Load/Check 'existing(uploaded) FAQ'
        3. Check 'unauthorized on FAQ patch'
        4. Check 'patch succeed'
        """
        rv = self.client.get('/faq')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

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

        rv = self.client.patch('/admin/faq')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': post_id, 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 200)
        # Patch success

    def testD_delete(self):
        """
        TC about FAQ delete

        1. Check 'unauthorized on FAQ getting'
        2. Load/Check 'existing(uploaded) FAQ'
        3. Check 'unauthorized on FAQ delete'
        4. Check 'delete succeed'
        """
        rv = self.client.get('/faq')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

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

        rv = self.client.delete('/admin/faq')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # Post id doesn't exist

        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 200)
        # Delete success
