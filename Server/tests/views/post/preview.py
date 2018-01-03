import json
import unittest2 as unittest

from tests.views import account_admin, account_student

from app.models.post import FAQModel, NoticeModel, RuleModel
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

        FAQModel.objects.delete()
        NoticeModel.objects.delete()
        RuleModel.objects.delete()

    def testA_faqPreviewSet(self):
        """
        TC about FAQ preview setting

        - Preparations
        Add sample FAQ
        Take FAQ ID

        - Exception Tests
        Forbidden with student access token
        Short FAQ ID
        Non-existing FAQ ID

        - Process
        Set FAQ preview

        - Validation
        Check preview FAQ data
        """
        # -- Preparations --
        self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        faq_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/preview/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.post('/admin/preview/faq', headers={'Authorization': self.admin_access_token}, data={'id': '1234'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/admin/preview/faq', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/preview/faq', headers={'Authorization': self.admin_access_token}, data={'id': faq_id})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/preview/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode())['pinned'])
        # -- Validation --

    def testB_faqPreviewGet(self):
        """
        TC about FAQ preview getting

        - Preparations
        Get preview when FAQ data is empty
        Add sample FAQ preview

        - Exception Tests
        None

        - Process
        Get preview with admin access token
        Get preview with student access token

        - Validation
        None
        """
        # -- Preparations --
        rv = self.client.get('/preview/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        self.client.post('/admin/faq', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        rv = self.client.get('/faq', headers={'Authorization': self.admin_access_token})
        faq_id = json.loads(rv.data.decode())[0]['id']

        self.client.post('/admin/preview/faq', headers={'Authorization': self.admin_access_token}, data={'id': faq_id})
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/preview/faq', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)

        rv = self.client.get('/preview/faq', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testC_noticePreviewSet(self):
        """
        TC about notice preview setting

        - Preparations
        Add sample notice
        Take notice ID

        - Exception Tests
        Forbidden with student access token
        Short notice ID
        Non-existing notice ID

        - Process
        Set notice preview

        - Validation
        Check preview notice data
        """
        # -- Preparations --
        self.client.post('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        rv = self.client.get('/notice', headers={'Authorization': self.admin_access_token})
        notice_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/preview/notice', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.post('/admin/preview/notice', headers={'Authorization': self.admin_access_token}, data={'id': '1234'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/admin/preview/notice', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/preview/notice', headers={'Authorization': self.admin_access_token}, data={'id': notice_id})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/preview/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode())['pinned'])
        # -- Validation --

    def testD_noticePreviewGet(self):
        """
        TC about notice preview getting

        - Preparations
        Get preview when notice data is empty
        Add sample notice preview

        - Exception Tests
        None

        - Process
        Get preview with admin access token
        Get preview with student access token

        - Validation
        None
        """
        # -- Preparations --
        rv = self.client.get('/preview/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        self.client.post('/admin/notice', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        rv = self.client.get('/notice', headers={'Authorization': self.admin_access_token})
        notice_id = json.loads(rv.data.decode())[0]['id']

        self.client.post('/admin/preview/notice', headers={'Authorization': self.admin_access_token}, data={'id': notice_id})
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/preview/notice', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)

        rv = self.client.get('/preview/notice', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)
        # -- Process --

        # -- Validation --
        # -- Validation --

    def testE_rulePreviewSet(self):
        """
        TC about rule preview setting

        - Preparations
        Add sample rule
        Take rule ID

        - Exception Tests
        Forbidden with student access token
        Short rule ID
        Non-existing rule ID

        - Process
        Set rule preview

        - Validation
        Check preview rule data
        """
        # -- Preparations --
        self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        rule_id = json.loads(rv.data.decode())[0]['id']
        # -- Preparations --

        # -- Exception Tests --
        rv = self.client.post('/admin/preview/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 403)

        rv = self.client.post('/admin/preview/rule', headers={'Authorization': self.admin_access_token}, data={'id': '1234'})
        self.assertEqual(rv.status_code, 204)

        rv = self.client.post('/admin/preview/rule', headers={'Authorization': self.admin_access_token}, data={'id': '123456789012345678901234'})
        self.assertEqual(rv.status_code, 204)
        # -- Exception Tests --

        # -- Process --
        rv = self.client.post('/admin/preview/rule', headers={'Authorization': self.admin_access_token}, data={'id': rule_id})
        self.assertEqual(rv.status_code, 201)
        # -- Process --

        # -- Validation --
        rv = self.client.get('/preview/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(json.loads(rv.data.decode())['pinned'])
        # -- Validation --

    def testF_rulePreviewGet(self):
        """
        TC about rule preview getting

        - Preparations
        Get preview when rule data is empty
        Add sample rule preview

        - Exception Tests
        None

        - Process
        Get preview with admin access token
        Get preview with student access token

        - Validation
        None
        """
        # -- Preparations --
        rv = self.client.get('/preview/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 204)

        self.client.post('/admin/rule', headers={'Authorization': self.admin_access_token}, data={'title': 'test', 'content': 'test'})
        rv = self.client.get('/rule', headers={'Authorization': self.admin_access_token})
        rule_id = json.loads(rv.data.decode())[0]['id']

        self.client.post('/admin/preview/rule', headers={'Authorization': self.admin_access_token}, data={'id': rule_id})
        # -- Preparations --

        # -- Exception Tests --
        # -- Exception Tests --

        # -- Process --
        rv = self.client.get('/preview/rule', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)

        rv = self.client.get('/preview/rule', headers={'Authorization': self.student_access_token})
        self.assertEqual(rv.status_code, 200)
        self.assertTrue(rv.data)
        # -- Process --

        # -- Validation --
        # -- Validation --
