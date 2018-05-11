from app.models.report import FacilityReportModel

from tests.v2.views import TCBase


class TestFacilityReportInquire(TCBase):
    """
    관리자의 시설고장신고 조회를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestFacilityReportInquire, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/admin/report/facility'

    def setUp(self):
        super(TestFacilityReportInquire, self).setUp()

        # ---

        report1 = FacilityReportModel(
            author=self.student.name,
            content='신고1',
            room=200
        ).save()

        report2 = FacilityReportModel(
            author=self.student.name,
            content='신고2',
            room=500
        ).save()

        self.expected_response_data = [
            {
                'id': str(report1.id),
                'author': report1.author,
                'content': report1.content,
                'room': report1.room
            },
            {
                'id': str(report2.id),
                'author': report2.author,
                'content': report2.content,
                'room': report2.room
            }
        ]

        self._request = lambda *, token=None: self.request(
            self.method,
            self.target_uri,
            token
        )

    def testLoadSuccess(self):
        # (1) 시설고장신고 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertListEqual(self.expected_response_data, resp.json)

    def testForbidden(self):
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)
