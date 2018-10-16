from tests.v2.views import TCBase
from cron.meal_parser import _parse


class TestMeal(TCBase):
    """
    급식 정보 조회를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestMeal, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/meal/{}'
        self.date = '2018-05-31'
        self.expected_response_data = {
            'breakfast': ['흰밥(쌀밥)', '석류사과쥬스', '배추김치', '부추무침', '삼겹살매운구이', '다시마감자국'],
            'dinner': ['흰밥(쌀밥)', '애호박고추장찌개', '오향장육', '파채무침', '양배추찜', '쌈장', '보쌈김치'],
            'lunch': ['흰밥(쌀밥)', '설렁탕', '소면', '깐쇼새우', '알감자조림', '사과맛발효유', '석박지']
        }

    def setUp(self):
        super(TestMeal, self).setUp()

        # ---

        _parse(2018, 5)

        self._request = lambda *, token=None, date=self.date: self.request(
            self.method,
            self.target_uri.format(date),
            token
        )

    def testMealLoadWithValidDate(self):
        # (1) 급식 정보 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, self.expected_response_data)

    def testMeaLoadWithInvalidDate(self):
        # (1) 급식 정보가 존재하지 않는 날짜로 조회
        resp = self._request(date='2001-01-01')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)
