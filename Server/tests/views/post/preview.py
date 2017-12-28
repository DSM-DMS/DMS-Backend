import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from server import app


class TestPreview(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()

        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()

    def testA_faqPreviewSet(self):
        """
        TC about faq preview set

        1. Post sample FAQ
        2. Get ID of pre-posted FAQ
        3. Check 'preview set succeed'
        """
        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post sample FAQ

        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get existing notice list

        data = json.loads(rv.data.decode())

        post_id = ''
        for faq in data:
            if faq['title'] == 'test' and faq['author'] == 'fake':
                post_id = faq['id']

        rv = self.client.post('/admin/preview/faq', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 201)
        # Set preview success

    def testB_faqPreviewGet(self):
        """
        TC about faq preview get

        1. Check 'preview get succeed using admin's access token'
        2. Check 'preview get succeed using student's access token'
        """
        rv = self.client.get('/preview/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get preview success on admin's access token

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'test' and data['author'] == 'fake')
        # Validate preview data

        rv = self.client.get('/preview/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get preview success on student's access token

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'test' and data['author'] == 'fake')
        # Validate preview data

    def testC_noticePreviewSet(self):
        """
        TC about notice preview set

        1. Post sample notice
        2. Get ID of pre-posted notice
        3. Check 'preview set succeed'
        """
        rv = self.client.post('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post sample notice

        rv = self.client.get('/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get existing notice list

        data = json.loads(rv.data.decode())

        post_id = ''
        for notice in data:
            if notice['title'] == 'test' and notice['author'] == 'fake':
                post_id = notice['id']

        rv = self.client.post('/admin/preview/notice', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 201)
        # Set preview success

    def testD_noticePreviewGet(self):
        """
        TC about notice preview get

        1. Check 'preview get succeed using admin's access token'
        2. Check 'preview get succeed using student's access token'
        """
        rv = self.client.get('/preview/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get preview success on admin's access token

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'test' and data['author'] == 'fake')
        # Validate preview data

        rv = self.client.get('/preview/notice', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get preview success on student's access token

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'test' and data['author'] == 'fake')
        # Validate preview data

    def testE_rulePreviewSet(self):
        """
        TC about rule preview set

        1. Post sample rule
        2. Get ID of pre-posted rule
        3. Check 'preview set succeed'
        """
        rv = self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Post sample rule

        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get existing rule list

        data = json.loads(rv.data.decode())

        post_id = ''
        for rule in data:
            if rule['title'] == 'test' and rule['author'] == 'fake':
                post_id = rule['id']

        rv = self.client.post('/admin/preview/rule', headers={'Authorization': self.admin_access_token}, data={'id': post_id})
        self.assertEqual(rv.status_code, 201)
        # Set preview success

    def testF_rulePreviewGet(self):
        """
        TC about rule preview get

        1. Check 'preview get succeed using admin's access token'
        2. Check 'preview get succeed using student's access token'
        """
        rv = self.client.get('/preview/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get preview success on admin's access token

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'test' and data['author'] == 'fake')
        # Validate preview data

        rv = self.client.get('/preview/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        # Get preview success on student's access token

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'test' and data['author'] == 'fake')
        # Validate preview data
