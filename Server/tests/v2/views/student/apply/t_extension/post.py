from app.models.apply import ExtensionApply11Model, ExtensionApply12Model

from tests.v2.views import TCBase


class ExtensionApplyTCBase(TCBase):
    def __init__(self, hour, *args, **kwargs):
        super(ExtensionApplyTCBase, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/apply/extension/{}'.format(hour)

        self.target_model = ExtensionApply11Model if hour == 11 else ExtensionApply12Model
        self.class_ = 1
        self.seat = 1

    def setUp(self):
        super(ExtensionApplyTCBase, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token, class_=self.class_, seat=self.seat: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'classNum': class_,
                'seatNum': seat
            }
        )

    def _testCommonApply(self):
        # (1) 신청
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) 데이터베이스 확인
        self.assertTrue(self.target_model.objects(student=self.student, class_=self.class_, seat=self.seat))

    def _testAlreadyAppliedSeat(self):
        self.target_model(
            student=self.student,
            class_=self.class_,
            seat=self.seat
        ).save()

        # (1) 이미 신청된 자리에 재신청
        resp = self._request()

        # (2) status code 400
        self.assertEqual(resp.status_code, 400)

    def _testInvalidClass(self):
        # (1) 신청할 수 없는 교실에 신청
        resp = self._request(class_=0)

        # (2) status code 400
        self.assertEqual(resp.status_code, 400)

    def _testDuplicatedApply(self):
        self.target_model(
            student=self.student,
            class_=self.class_,
            seat=self.seat
        ).save()

        # (1) 다른 자리에 신청
        resp = self._request(seat=self.seat + 1)

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) 데이터베이스 확인
        self.assertTrue(self.target_model.objects(student=self.student, class_=self.class_, seat=self.seat + 1))

    def _testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)


class TestExtensionApply11(ExtensionApplyTCBase):
    def __init__(self, *args, **kwargs):
        super(TestExtensionApply11, self).__init__(11, *args, **kwargs)

    def setUp(self):
        super(TestExtensionApply11, self).setUp()

    def testCommonApply(self):
        self._testCommonApply()

    def testAlreadyAppliedSeat(self):
        self._testAlreadyAppliedSeat()

    def testInvalidClass(self):
        self._testInvalidClass()

    def testDuplicatedApply(self):
        self._testDuplicatedApply()

    def testForbidden(self):
        self._testForbidden()


class TestExtensionApply12(ExtensionApplyTCBase):
    def __init__(self, *args, **kwargs):
        super(TestExtensionApply12, self).__init__(12, *args, **kwargs)

    def setUp(self):
        super(TestExtensionApply12, self).setUp()

    def testCommonApply(self):
        # TODO
        self._testCommonApply()

    def testAlreadyAppliedSeat(self):
        # TODO
        self._testAlreadyAppliedSeat()

    def testInvalidClass(self):
        self._testInvalidClass()

    def testDuplicatedApply(self):
        # TODO
        self._testDuplicatedApply()

    def testForbidden(self):
        self._testForbidden()
