import json
import unittest

from tests.views import account_admin, account_student

from app.models.post import FAQModel
from server import app


class TestFAQ(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()
        FAQModel.objects.delete()

    def testA_post(self):
        """
        TC about FAQ uploading

        - Preparations
        None

        - Exception Tests
        Forbidden with student access token

        - Process
        Post FAQ data

        - Validation
        Check post data is existing
        """
        # -- Preparations --
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode()))
        # -- Validation --

    def testB_get(self):
        """
        TC about FAQ data getting

        - Preparations
        Post sample FAQ data

        - Exception Tests
        Short FAQ ID with admin/student access token
        Non-existing FAQ ID with admin/student access token

        - Process
        Load FAQ data with admin access token
        Load FAQ data with student access token

        - Validation
        None
        """
        # -- Preparations --
        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.get('/faq/1234', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.get('/faq/1234', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.get('/faq/123456789012345678901234', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.get('/faq/123456789012345678901234', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        faq_id = json.loads(rv.data.decode())[0]['id']

        rv = self.client.get('/faq/' + faq_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode()))

        rv = self.client.get('/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        faq_id = json.loads(rv.data.decode())[0]['id']

        rv = self.client.get('/faq/' + faq_id, headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode()))
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testC_patch(self):
        """
        TC about FAQ data patching

        - Preparations
        Post sample FAQ data
        Take FAQ ID

        - Exception Tests
        Forbidden with student access token
        Short FAQ ID
        Non-existing FAQ ID

        - Process
        Change FAQ data

        - Validation
        Check changed FAQ data
        """
        # -- Preparations --
        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        faq_id = json.loads(rv.data.decode())['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.patch('/admin/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '1234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.patch('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': faq_id, 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/faq/' + faq_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertTrue(data['title'] == data['content'] == 'new')
        # -- Validation --

    def testD_delete(self):
        """
        TC about FAQ data deletion

        - Preparations
        Post sample FAQ data
        Take FAQ ID

        - Exception Tests
        Forbidden with student access token
        Short FAQ ID
        Non-existing FAQ ID

        - Process
        Delete FAQ data

        - Validation
        Check FAQ data is empty
        """
        # -- Preparations --
        rv = self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        faq_id = json.loads(rv.data.decode())['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.delete('/admin/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '1234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234', 'title': 'new', 'content': 'new'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.delete('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'id': faq_id})
        self.assertEqual(rv.status_code, 200)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/faq/' + faq_id, headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)
        # -- Validation --
