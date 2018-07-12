from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel
from app.models.point import PointHistoryModel

from tests.v2.views import TCBase


class TestApplyStatus(TCBase):
    """
    신청 정보 확인을 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestApplyStatus, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/student/info/apply'

    def setUp(self):
        super(TestApplyStatus, self).setUp()

        # ---

        self._request = lambda *, token=None: self.request(
            self.method,
            self.target_uri,
            token
        )

    def testDefaultStatus(self):
        # (1) 신청 정보 확인
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, {
            'extension11': None,
            'extension12': None,
            'goingout': {
                'sat': False,
                'sun': False
            },
            'stay': 4
        })

    def testAfterApply(self):
        extension_apply_11 = ExtensionApply11Model(
            student=self.student,
            class_=1,
            seat=15
        ).save()

        extension_apply_12 = ExtensionApply12Model(
            student=self.student,
            class_=3,
            seat=13
        ).save()

        goingout_apply = GoingoutApplyModel(
            student=self.student,
            on_saturday=True,
            on_sunday=False
        ).save()

        stay_apply = StayApplyModel(
            student=self.student,
            value=1
        ).save()

        # (1) 신청 정보 확인
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, {
            'extension11': {
                'classNum': extension_apply_11.class_,
                'seat': extension_apply_11.seat
            },
            'extension12': {
                'classNum': extension_apply_12.class_,
                'seat': extension_apply_12.seat
            },
            'goingout': {
                'sat': goingout_apply.on_saturday,
                'sun': goingout_apply.on_sunday
            },
            'stay': stay_apply.value
        })

    def testForbidden(self):
        # (1) 403 체크
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)

    """
    This TC tests
        * METHOD /
    """
    def setUp(self):
        super(TestStudentAccountAuth, self).setUp()

        # ---

    def tearDown(self):
        # ---

        super(TestStudentAccountAuth, self).tearDown()

    def test(self):
        # -- Test --
        pass
