from tests.v2.views import TCBase
from tests.v2.views.admin.point import add_point_rules


class TestPointGiving(TCBase):
    """
    상벌점 부여를 테스트합니다.
        * POST /admin/point
    """
    def setUp(self):
        super(TestPointGiving, self).setUp()

        # ---

        self.good_point_rule, self.bad_point_rule = add_point_rules()

        self._request = lambda *, token=None, id=self.student_id, rule_id=self.good_point_rule.id, point=1: self.request(
            self.client.post,
            '/admin/point',
            token,
            json={
                'id': id,
                'ruleId': rule_id,
                'point': point
            }
        )

    def testGoodPointGivingSuccess(self):
        # (1) 상점 부여
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = self.get_response_data_as_json(resp)

        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

    def testBadPointGivingSuccess(self):
        # (1) 벌점 부여
        resp = self._request(rule_id=self.bad_point_rule.id)

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = self.get_response_data_as_json(resp)

        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

    def testPointGivingFailure_ruleDoesNotExist(self):
        # (1) 존재하지 않는 규칙 ID를 통해 상점
        resp = self._request(rule_id='123')

        # (2) status code 205
        self.assertEqual(resp.status_code, 205)

    def testPointGivingFailure_studentDoesNotExist(self):
        # (1) 존재하지 않는 학생 ID를 통해 상점 부여
        resp = self._request(id=self.admin_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class TestPointHistoryInquire(TCBase):
    """
    상벌점 내역 조회를 테스트합니다.
        * GET /admin/point
    """
    def setUp(self):
        super(TestPointHistoryInquire, self).setUp()

        # ---

        self.good_point_rule, self.bad_point_rule = add_point_rules()

        self.request(
            self.client.post,
            '/admin/point',
            json={
                'id': id,
                'ruleId': self.good_point_rule.id,
                'point': 1
            }
        )

        self._request = lambda *, token=None, id=self.student_id: self.request(
            self.client.get,
            '/admin/point',
            token,
            query_string={
                'id': id
            }
        )

    def testHistoryInquireSuccess(self):
        pass

    def testHistoryInquireFailure_studentDoesNotExist(self):
        pass

    def testForbidden(self):
        pass


class TestPointHistoryDeletion(TCBase):
    """
    상벌점 내역 제거를 테스트합니다.
        * DELETE /admin/point
    """
    def setUp(self):
        super(TestPointHistoryDeletion, self).setUp()

        # ---

        self.good_point_rule, self.bad_point_rule = add_point_rules()

        resp = self.request(
            self.client.post,
            '/admin/point',
            json={
                'id': id,
                'ruleId': self.good_point_rule.id,
                'point': 1
            }
        )

        self.history_id = self.get_response_data_as_json(resp)['id']

        self._request = lambda *, token=None, id=self.student_id, history_id=self.history_id: self.request(
            self.client.delete,
            '/admin/point',
            token,
            json={
                'studentId': id,
                'historyId': history_id
            }
        )

    def testDeleteSuccess(self):
        pass

    def testDeleteFailure_studentDoesNotExist(self):
        pass

    def testDeleteFailure_historyDoesNotExist(self):
        pass

    def testForbidden(self):
        pass
