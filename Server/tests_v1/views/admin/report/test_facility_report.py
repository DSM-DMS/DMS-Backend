from tests_v1.views import TCBase

from app_v1.models.report import FacilityReportModel


class TestFacilityReport(TCBase):
    """
    TC about facility report inquiring

    This TC tests_v1
        * GET /admin/report/facility
    """
    def setUp(self):
        """
        - Before Test

        Upload new facility report
            * POST /report/facility
        """
        TCBase.setUp(self)

        # ---

        self.report = {
            'title': 'title',
            'content': 'content',
            'room': 200
        }

        self.request(
            self.client.post,
            '/report/facility',
            self.report
        )

    def tearDown(self):
        """
        - After Test
        """
        FacilityReportModel.objects.delete()

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
                    'id': str(length: 24),
                    'author': str(value: 'fake_student'),
                    'title': 'title',
                    'content': 'content',
                    'room': 200
                }
            ]
        """
        # -- Test --
        resp = self.request(
            self.client.get,
            '/admin/report/facility',
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

        self.assertIn('id', report)
        id = report['id']
        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 24)

        del report['id']

        self.report.update({'author': 'fake_student'})
        self.assertDictEqual(report, self.report)
        # -- Test --
