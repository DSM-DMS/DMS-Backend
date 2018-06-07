from app.models.account import StudentModel
from app.models.point import PointHistoryModel

from tests.v2.views import TCBase
from tests.v2.views.admin.point import add_point_rules


class TestPointGiving(TCBase):
    """
    상벌점 부여를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestPointGiving, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/admin/point/point/{}'

    def setUp(self):
        super(TestPointGiving, self).setUp()

        # ---

        self.good_point_rule, self.bad_point_rule = add_point_rules()

        self._request = lambda *, token=None, id=self.student_id, rule_id=self.good_point_rule.id, apply_good_point=True, point=1: self.request(
            self.method,
            self.target_uri.format(id),
            token,
            json={
                'ruleId': str(rule_id),
                'applyGoodPoint': apply_good_point,
                'point': point
            }
        )

    def testGoodPointGivingSuccess(self):
        # (1) 상점 부여
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = resp.json
        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

        # (4) 데이터베이스 확인
        student = StudentModel.objects(id=self.student_id).first()
        self.assertEqual(len(student.point_histories), 1)

        history = student.point_histories[0]
        self.assertEqual(history.point_type, True)
        self.assertEqual(history.point, 1)

        self.assertEqual(student.good_point, 1)

    def testBadPointGivingSuccess(self):
        # (1) 벌점 부여
        resp = self._request(rule_id=self.bad_point_rule.id, apply_good_point=False, point=-1)

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = resp.json

        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

        # (4) 데이터베이스 확인
        student = StudentModel.objects(id=self.student_id).first()
        self.assertEqual(len(student.point_histories), 1)

        history = student.point_histories[0]
        self.assertEqual(history.point_type, False)
        self.assertEqual(history.point, -1)

        self.assertEqual(student.bad_point, 1)

    def testPointGivingFailure_studentDoesNotExist(self):
        # (1) 존재하지 않는 학생 ID를 통해 상점 부여
        resp = self._request(id=self.admin_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testPointGivingFailure_ruleDoesNotExist(self):
        # (1) 존재하지 않는 규칙 ID를 통해 상점 부여
        resp = self._request(rule_id='123')

        # (2) status code 205
        self.assertEqual(resp.status_code, 205)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class TestPointHistoryInquire(TCBase):
    """
    상벌점 내역 조회를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestPointHistoryInquire, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/admin/point/point/{}'

    def setUp(self):
        super(TestPointHistoryInquire, self).setUp()

        # ---

        good_point_history = PointHistoryModel(
            reason='상점 규칙',
            point_type=True,
            point=1
        )

        self.student.point_histories.append(good_point_history)

        bad_point_history = PointHistoryModel(
            reason='벌점 규칙',
            point_type=False,
            point=1
        )

        self.student.point_histories.append(bad_point_history)

        self.student.save()

        self.expected_good_point_history = {
            'date': self.today,
            'reason': good_point_history.reason,
            'pointType': good_point_history.point_type,
            'point': good_point_history.point
        }

        self.expected_bad_point_history = {
            'date': self.today,
            'reason': bad_point_history.reason,
            'pointType': bad_point_history.point_type,
            'point': bad_point_history.point
        }

        self._request = lambda *, token=None, id=self.student_id: self.request(
            self.method,
            self.target_uri.format(id),
            token
        )

    def _validate_history_data(self, data, expected_dict):
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

        del data['id']

        self.assertDictEqual(data, expected_dict)

    def testHistoryInquireSuccess(self):
        # (1) 상벌점 내역 조회
        resp = self._request(id=self.student_id)

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        data = resp.json
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)

        good_point_history, bad_point_history = data
        self._validate_history_data(good_point_history, self.expected_good_point_history)
        self._validate_history_data(bad_point_history, self.expected_bad_point_history)

    def testHistoryInquireFailure_studentDoesNotExist(self):
        # (1) 존재하지 않는 학생 ID를 통해 상벌점 내역 조회
        resp = self._request(id=self.admin_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class TestPointHistoryDeletion(TCBase):
    """
    상벌점 내역 제거를 테스트합니다.
        * DELETE /admin/point/point
    """
    def __init__(self, *args, **kwargs):
        super(TestPointHistoryDeletion, self).__init__(*args, **kwargs)

        self.method = self.client.delete
        self.target_uri = '/admin/point/point/{}'

    def setUp(self):
        super(TestPointHistoryDeletion, self).setUp()

        # ---

        self.student.point_histories.append(
            PointHistoryModel(
                reason='상점 규칙',
                point_type=True,
                point=1
            )
        )

        self.student.point_histories.append(
            PointHistoryModel(
                reason='벌점 규칙',
                point_type=False,
                point=1
            )
        )

        self.student.good_point = self.student.bad_point = 1

        self.student.save()

        self.good_point_history_id, self.bad_point_history_id = [history.id for history in self.student.point_histories]

        self._request = lambda *, token=None, id=self.student_id, history_id=self.good_point_history_id: self.request(
            self.method,
            self.target_uri.format(id),
            token,
            json={
                'historyId': str(history_id)
            }
        )

    def testDeleteSuccess(self):
        # (1) 상점 내역 삭제
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        student = StudentModel.objects(id=self.student_id).first()
        self.assertEqual(len(student.point_histories), 1)
        self.assertFalse(student.good_point)

        # (4) 벌점 내역 삭제
        resp = self._request(history_id=self.bad_point_history_id)

        # (5) status code 200
        self.assertEqual(resp.status_code, 200)

        # (6) 데이터베이스 확인
        student = StudentModel.objects(id=self.student_id).first()
        self.assertFalse(student.point_histories)
        self.assertFalse(student.bad_point)

    def testDeleteFailure_studentDoesNotExist(self):
        # (1) 존재하지 않는 학생 ID를 통해 내역 삭제
        resp = self._request(id=self.admin_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testDeleteFailure_historyDoesNotExist(self):
        # (1) 존재하지 않는 내역 ID를 통해 내역 삭제
        resp = self._request(history_id='123')

        # (2) status code 205
        self.assertEqual(resp.status_code, 205)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)
