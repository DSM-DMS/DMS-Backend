import json
import unittest2 as unittest

from app.models.account import AdminModel, StudentModel
from app.models.report import BugReportModel
from tests.views import admin, student

from server import app


class TestBugReport(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        admin.create_fake_account()
        student.create_fake_account()

        self.student_access_token = student.get_access_token(self.client)
        self.admin_access_token = admin.get_access_token(self.client)

    def tearDown(self):
        StudentModel.objects(
            id='fake'
        ).delete()

        AdminModel.objects(
            id='fake'
        ).delete()

        BugReportModel.objects(
            title='test',
            content='test'
        ).delete()

    def testReport(self):
        rv = self.client.post('/report/bug')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/report/bug', headers={'Authorization': self.student_access_token}, data={'title': 'test', 'content': 'test'})
        self.assertEqual(rv.status_code, 201)
        # Report success

        rv = self.client.get('/admin/report/bug')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.get('/admin/report/bug', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)

        flag = False
        for report in json.loads(rv.data):
            if report['title'] == report['content'] == 'test':
                flag = True

        self.assertTrue(flag)
