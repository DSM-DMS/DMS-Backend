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

        self._request = lambda *, token=self.student_access_token: self.request(
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
                'seatNum': extension_apply_11.seat
            },
            'extension12': {
                'classNum': extension_apply_12.class_,
                'seatNum': extension_apply_12.seat
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


class TestMypage(TCBase):
    """
    마이페이지 API를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestMypage, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/student/info/mypage'

    def setUp(self):
        super(TestMypage, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token: self.request(
            self.method,
            self.target_uri,
            token
        )

    def _test(self):
        # (1) 정보 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, {
            'badPoint': self.student.bad_point,
            'goodPoint': self.student.good_point,
            'name': self.student.name,
            'number': self.student.number
        })

    def testDefaultStatus(self):
        self._test()

    def testAfterDataChange(self):
        self.student.bad_point = 3
        self.student.good_point = 10
        self.student.name = 'DMS'
        self.student.number = 3214
        self.student.save()

        self._test()

    def testForbidden(self):
        # (1) 403 체크
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)


class TestPointHistory(TCBase):
    """
    상벌점 내역 조회를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestPointHistory, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/student/info/point-history'

    def setUp(self):
        super(TestPointHistory, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token: self.request(
            self.method,
            self.target_uri,
            token
        )

    def testDefaultStatus(self):
        # (1) 내역 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertListEqual(resp.json, [])

    def testAfterDataChange(self):
        from tests.v2.views.admin.point import add_point_rules
        good_point_rule, bad_point_rule = add_point_rules()

        self.student.point_histories.append(PointHistoryModel(
            reason=good_point_rule.name,
            point_type=good_point_rule.point_type,
            point=good_point_rule.min_point
        ))

        self.student.point_histories.append(PointHistoryModel(
            reason=bad_point_rule.name,
            point_type=bad_point_rule.point_type,
            point=bad_point_rule.min_point
        ))

        self.student.save()

        # (1) 내역 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertListEqual(resp.json, [
            {
                'point': good_point_rule.min_point,
                'pointType': good_point_rule.point_type,
                'reason': good_point_rule.name,
                'time': self.today
            },
            {
                'point': bad_point_rule.min_point,
                'pointType': bad_point_rule.point_type,
                'reason': bad_point_rule.name,
                'time': self.today
            }
        ])

    def testForbidden(self):
        # (1) 403 체크
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)
