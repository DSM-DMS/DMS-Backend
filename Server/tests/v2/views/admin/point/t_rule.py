from app.models.point import PointRuleModel

from tests.v2.views import TCBase
from tests.v2.views.admin.point import add_point_rules


class TestRuleAddition(TCBase):
    """
    상벌점 규칙 추가를 테스트합니다.
        * POST /admin/point/rule
    """
    def setUp(self):
        super(TestRuleAddition, self).setUp()

        # ---

        self.good_point_rule_name = '상점 규칙'
        self.bad_point_rule_name = '벌점 규칙'
        self.min_point = 1
        self.max_point = 3

        self._request = lambda *, token=None, name=self.good_point_rule_name, point_type=True, min_point=self.min_point, max_point=self.max_point: self.request(
            self.client.post,
            '/admin/point/rule',
            token,
            json={
                'name': name,
                'pointType': point_type,
                'minPoint': min_point,
                'maxPoint': max_point
            }
        )

    def testGoodPointRuleAdditionSuccess(self):
        # (1) 상점 규칙 추가
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = self.get_response_data_as_json(resp)
        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

        # (4) 데이터베이스 확인
        rules = PointRuleModel.objects

        self.assertEqual(rules.count(), 1)

        rule = rules[0]

        self.assertEqual(rule.name == self.good_point_rule_name)
        self.assertTrue(rule.point_type)
        self.assertEqual(rule.min_point, self.min_point)
        self.assertEqual(rule.max_point, self.max_point)

    def testBadPointRuleAdditionSuccess(self):
        # (1) 벌점 규칙 추가
        resp = self._request(name='벌점 규칙', point_type=False)

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = self.get_response_data_as_json(resp)
        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

        # (4) 데이터베이스 확인
        rules = PointRuleModel.objects

        self.assertEqual(rules.count(), 1)

        rule = rules[0]

        self.assertEqual(rule.name == self.bad_point_rule_name)
        self.assertFalse(rule.point_type)
        self.assertEqual(rule.min_point, self.min_point)
        self.assertEqual(rule.max_point, self.max_point)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class TestRuleInquire(TCBase):
    """
    상벌점 규칙 조회를 테스트합니다.
        * GET /admin/point/rule
    """
    def setUp(self):
        super(TestRuleInquire, self).setUp()

        # ---

        self.good_point_rule, self.bad_point_rule = add_point_rules()

        self._request = lambda *, token=None: self.request(
            self.client.get,
            '/admin/point/rule',
            token
        )

    def _validate_rule_data(self, data, rule_obj):
        self.assertIsInstance(data, dict)

        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)

        self.assertDictEqual(data, {
            'name': rule_obj.name,
            'pointType': rule_obj.point_type,
            'minPoint': rule_obj.min_point,
            'maxPoint': rule_obj.max_point
        })

    def testInquireSuccess(self):
        # (1) 상벌점 규칙 목록 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        data = self.get_response_data_as_json(resp)
        self.assertIsInstance(data, list)

        good_point_rule, bad_point_rule = data

        self._validate_rule_data(good_point_rule, self.good_point_rule)
        self._validate_rule_data(bad_point_rule, self.bad_point_rule)

    def testForbidden(self):
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class Test(TCBase):
    """
    상벌점 규칙 수정을 테스트합니다.
        * PATCH /admin/point/rule
    """
    def setUp(self):
        super(Test, self).setUp()

        # ---

        self.good_point_rule, self.bad_point_rule = add_point_rules()

        self.new_rule_name = '새로운 규칙'
        self.new_min_point = 2
        self.new_max_point = 10

        self._request = lambda *, token=None, rule_id=self.good_point_rule.id, name=self.new_rule_name, point_type=True, min_point=self.new_min_point, max_point=self.new_max_point: self.request(
            self.client.patch,
            '/admin/point/rule',
            token,
            json={
                'ruleId': rule_id,
                'name': name,
                'pointType': point_type,
                'minPoint': min_point,
                'maxPoint': max_point
            }
        )

    def testPatchSuccess(self):
        # (1) 상벌점 규칙 수정
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        self.assertEqual(self.good_point_rule.name, self.new_rule_name)
        self.assertEqual(self.good_point_rule.min_point, self.new_min_point)
        self.assertEqual(self.good_point_rule.max_point, self.new_max_point)

    def testPatchFailure_ruleDoesNotExist(self):
        # (1) 존재하지 않는 규칙 ID를 통해 수정
        resp = self._request(rule_id='123')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)
