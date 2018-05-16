from tests.v2.views import TCBase


class TestDeveloperLoad(TCBase):
    """
    개발자 목록 조회를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestDeveloperLoad, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/metadata/links'

        self.expected_response_data = {
            'facebook': 'https://www.facebook.com/DMSforDSM/',
            'github': 'https://github.com/DSM-DMS',
            'android': 'https://play.google.com/store/apps/details?id=teamdms.dms_kotlin',
            'ios': 'https://itunes.apple.com/KR/app/id1328234395?mt=8'
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
