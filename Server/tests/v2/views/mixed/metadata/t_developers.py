from tests.v2.views import TCBase


class TestDeveloperLoad(TCBase):
    """
    개발자 목록 조회를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestDeveloperLoad, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/metadata/developer-info'

        self.expected_response_data = {
            'app': ['조성빈', '이병찬', '윤정현', '이성현'],
            'server': ['김성래', '조민규', '인상민'],
            'webFrontend': ['김지수', '김건', '서윤호', '김형규', '오인서', '윤효상'],
            'desktop': ['김경식', '정원태', '김동현', '이종현', '류근찬'],
            'design': ['윤여환', '김동규']
        }

    def setUp(self):
        super(TestDeveloperLoad, self).setUp()

        # ---

        self._request = lambda: self.request(
            self.method,
            self.target_uri
        )

    def testLoadSuccess(self):
        # (1) 개발자 정보 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self.assertDictEqual(resp.json, self.expected_response_data)
