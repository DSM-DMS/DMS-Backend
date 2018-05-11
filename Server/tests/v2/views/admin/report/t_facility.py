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


class TestFacilityReportDelete(TCBase):
    """
    관리자의 시설고장신고 삭제를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestFacilityReportDelete, self).__init__(*args, **kwargs)

        self.method = self.client.delete
        self.target_uri = '/admin/report/facility/{}'

    def setUp(self):
        super(TestFacilityReportDelete, self).setUp()

        # ---

        self.report1 = FacilityReportModel(
            author=self.student.name,
            content='신고1',
            room=200
        ).save()

        self.report2 = FacilityReportModel(
            author=self.student.name,
            content='신고2',
            room=500
        ).save()

        self._request = lambda *, token=None, id=self.report1.id: self.request(
            self.method,
            self.target_uri.format(id),
            token
        )

    def testDeleteSuccess(self):
        # (1) 시설고장신고 삭제
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        self.assertEqual(len(FacilityReportModel.objects), 1)

        report = FacilityReportModel.objects(id=self.report1.id).first()

        self.assertFalse(report)

    def testDeleteFailure_idDoesNotExist(self):
        # (1) 존재하지 않는 ID를 통해 시설고장신고 삭제
        resp = self._request(id='123')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)
