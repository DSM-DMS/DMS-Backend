from tests.views import TCBase

from app.models.report import BugReportModel


class TestBugReport(TCBase):
    """
    TC about bug report inquiring

    This TC tests
        * GET /admin/report/bug
    """
    def setUp(self):
        """
        - Before Test

        Upload new facility report
            * POST /report/bug
        """
        TCBase.setUp(self)

        # ---

        self.report = {
            'title': 'title',
            'content': 'content'
        }

        self.request(
            self.client.post,
            '/report/bug',
            self.report
        )

    def tearDown(self):
        """
        - After Test
        """
        BugReportModel.objects.delete()

        # ---

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Load facility reports
            * Validation
            (1) status code : 200
            (2) response data type : list
            (3) length of resource : 1
            (4) response data format
            [
                {
                    'author': str(value: 'fake_student'),
                    'title': 'title',
                    'content': 'content',
                }
            ]
        """
        # -- Test --
        resp = self.request(
            self.client.get,
            '/admin/report/bug',
            {},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        data = self.get_response_data(resp)
        self.assertIsInstance(data, list)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
        report = data[0]

        self.report.update({'author': 'fake_student'})
        self.assertDictEqual(report, self.report)
        # -- Test --
