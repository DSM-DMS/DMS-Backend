from app.models.report import FacilityReportModel

from tests.v2.views import TCBase


class TestFacilityReport(TCBase):
    """
    시설 고장 신고를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestFacilityReport, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/report/facility'

        self.content = 'hello'
        self.room = 311

    def setUp(self):
        super(TestFacilityReport, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token, content=self.content, room=self.room: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'content': content,
                'room': room
            }
        )

    def testReportSuccess(self):
        # (1) 시설고장 신고
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = resp.json

        self.assertIn('id', data)

        id = data['id']

        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 24)

        # (4) 데이터베이스 확인
        self.assertTrue(FacilityReportModel.objects(id=id, content=self.content, room=self.room))

    def testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)
