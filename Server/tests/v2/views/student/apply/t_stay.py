from app.models.apply import StayApplyModel

from tests.v2.views import TCBase


class TestStayApplyInquire(TCBase):
    """
    잔류신청 정보 조회를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestStayApplyInquire, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/student/apply/stay'

    def setUp(self):
        super(TestStayApplyInquire, self).setUp()

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
            'value': 4
        })

    def testInquireWithAppliment(self):
        apply = StayApplyModel(
            student=self.student,
            value=1
        ).save()

        # (1) 별도의 신청 정보가 있는 상태에서 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, {
            'value': apply.value
        })

    def testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)


class TestStayApply(TCBase):
    """
    잔류신청을 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestStayApply, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/apply/stay'

        self.value = 2

    def setUp(self):
        super(TestStayApply, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token, value=self.value: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'value': value,
            }
        )

    def testApplySuccess(self):
        # (1) 잔류신청
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) 데이터베이스 확인
        self.assertTrue(StayApplyModel.objects(student=self.student, value=self.value))

    def testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)
