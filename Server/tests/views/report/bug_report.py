import json
import unittest

from app.models.report import BugReportModel
from tests.views import account_admin, account_student

from server import app


class TestBugReport(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        account_admin.create_fake_account()
        account_student.create_fake_account()

        self.student_access_token = account_student.get_access_token(self.client)
        self.admin_access_token = account_admin.get_access_token(self.client)

    def tearDown(self):
        account_student.remove_fake_account()
        account_admin.remove_fake_account()

        BugReportModel.objects(
            title='test',
            content='test'
        ).delete()

    def testA_report(self):
        """
        TC about bug report

        1. Check 'report succeed'
        2. Check 'unauthorized on bug report getting'
        """
        rv = self.client.post('/report/bug', headers={'Authorization': self.student_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Report success

        rv = self.client.get('/admin/report/bug', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)

        flag = False
        for report in json.loads(rv.data.decode()):
            if report['title'] == report['content'] == 'test':
                flag = True

        self.assertTrue(flag)
