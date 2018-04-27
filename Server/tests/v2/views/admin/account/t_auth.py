from tests.v2.views import TCBase


class TestAdminAuth(TCBase):
    """
    관리자 계정 로그인을 테스트합니다.
        * POST /admin/auth
    """
    def setUp(self):
        super(TestAdminAuth, self).setUp()

        # ---

        self._request = lambda id=self.admin_id, pw=self.pw: self.json_request(
            self.client.post,
            '/admin/auth',
            data={
                'id': id,
                'pw': pw
            }
        )

        self.token_regex = '(?:\w+\.){2}\w+'

    def tearDown(self):
        # ---

        super(TestAdminAuth, self).tearDown()

    def _validate_response_data(self, resp):
        data = self.get_response_data_as_json(resp)
        self.assertIn('accessToken', data)
        self.assertIn('refreshToken', data)

        access_token = data['accessToken']
        refresh_token = data['refresh_token']

        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)

        self.assertRegex(access_token, self.token_regex)
        self.assertRegex(refresh_token, self.token_regex)

    def test(self):
        # -- Test --

        # (1) 관리자 계정으로 로그인
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        self._validate_response_data(resp)

        # -- Test --

        # -- Exception Test --

        # (1) 존재하지 않는 ID로 로그인
        resp = self._request(self.student_id)

        # (2) status code 401
        self.assertEqual(resp.status_code, 401)

        # ---

        # (1) 틀린 비밀번호로 로그인
        resp = self._request(pw='1')

        # (2) status code 401
        self.assertEqual(resp.status_code, 401)

        # -- Exception Test --
