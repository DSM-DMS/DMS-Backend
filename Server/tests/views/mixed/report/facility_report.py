import json
import unittest2 as unittest

from app.models.report import FacilityReportModel
from tests.views import admin, student

from server import app


class TestFacilityReport(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        admin.create_fake_account()
        student.create_fake_account()

        self.student_access_token = student.get_access_token(self.client)
        self.admin_access_token = admin.get_access_token(self.client)

    def tearDown(self):
        admin.remove_fake_account()
        student.remove_fake_account()

        FacilityReportModel.objects(
            title='test',
            content='test',
            room=415
        ).delete()

    def testA_report(self):
        """
        TC about facility report

        1. Check 'unauthorized on facility report'
        2. Check 'report succeed'
        3. Check 'unauthorized on facility report getting'
        """
        rv = self.client.post('/report/facility')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.post('/report/facility', headers={'Authorization': self.student_access_token}, data={'title': 'test', 'content': 'test', 'room': 415})
        self.assertEqual(rv.status_code, 201)
        # Report success

        rv = self.client.get('/admin/report/facility')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        rv = self.client.get('/admin/report/facility', headers={'Authorization': self.admin_access_token})
        self.assertEqual(rv.status_code, 200)

        flag = False
        for report in json.loads(rv.data.decode()):
            if report['title'] == report['content'] == 'test' and report['room'] == 415:
                flag = True

        self.assertTrue(flag)
