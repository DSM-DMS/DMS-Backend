from app.models.apply import ExtensionApply11Model, ExtensionApply12Model

from tests.v2.views import TCBase


class ExtensionApplyCancelTCBase(TCBase):
    def __init__(self, hour, *args, **kwargs):
        super(ExtensionApplyCancelTCBase, self).__init__(*args, **kwargs)

        self.method = self.client.delete
        self.target_uri = '/student/apply/extension/{}'.format(hour)

        self.target_model = ExtensionApply11Model if hour == 11 else ExtensionApply12Model

    def setUp(self):
        super(ExtensionApplyCancelTCBase, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token: self.request(
            self.method,
            self.target_uri,
            token
        )

    def _testWithoutApply(self):
        # (1) 신청되지 않은 상태에서 신청 취소
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        self.assertFalse(self.target_model.objects)

    def _testWithApply(self):
        self.target_model(
            student=self.student,
            class_=1,
            seat=1
        ).save()

        # (1) 신청된 상태에서 신청 취소
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        self.assertFalse(self.target_model.objects)

    def _testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)


class TestExtensionApplyCancel11(ExtensionApplyCancelTCBase):
    def __init__(self, *args, **kwargs):
        super(TestExtensionApplyCancel11, self).__init__(11, *args, **kwargs)

    def setUp(self):
        super(TestExtensionApplyCancel11, self).setUp()

    def testWithoutApply(self):
        self._testWithoutApply()

    def testWithApply(self):
        self._testWithApply()

    def testForbidden(self):
        self._testForbidden()


class TestExtensionApplyCancel12(ExtensionApplyCancelTCBase):
    def __init__(self, *args, **kwargs):
        super(TestExtensionApplyCancel12, self).__init__(12, *args, **kwargs)

    def setUp(self):
        super(TestExtensionApplyCancel12, self).setUp()

    def testWithoutApply(self):
        self._testWithoutApply()

    def testWithApply(self):
        self._testWithApply()

    def testForbidden(self):
        self._testForbidden()
