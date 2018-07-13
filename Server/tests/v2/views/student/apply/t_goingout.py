from app.models.apply import GoingoutApplyModel

from tests.v2.views import TCBase


class TestGoingoutApplyInquire(TCBase):
    """
    외출신청 정보 조회를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestGoingoutApplyInquire, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/student/apply/goingout'

    def setUp(self):
        super(TestGoingoutApplyInquire, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token: self.request(
            self.method,
            self.target_uri,
            token
        )

    def testInquireWithoutAnyAppliment(self):
        # (1) 별도의 신청 정보 없이 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, {
            'sat': False,
            'sun': False
        })

    def testInquireWithAppliment(self):
        apply = GoingoutApplyModel(
            student=self.student,
            on_saturday=True,
            on_sunday=False
        ).save()

        # (1) 별도의 신청 정보가 있는 상태에서 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, {
            'sat': apply.on_saturday,
            'sun': apply.on_sunday
        })

    def testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)


class TestGoingoutApply(TCBase):
    """
    외출신청을 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestGoingoutApply, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/apply/goingout'

        self.sat = True
        self.sun = True

    def setUp(self):
        super(TestGoingoutApply, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token, sat=self.sat, sun=self.sun: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'sat': sat,
                'sun': sun
            }
        )

    def testApplySuccess(self):
        # (1) 외출신청
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) 데이터베이스 확인
        self.assertTrue(GoingoutApplyModel.objects(student=self.student, on_saturday=self.sat, on_sunday=self.sun))

    def testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)
    # TODO 예외 사항을 더 넣어야 할듯..
