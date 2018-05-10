from tests.v2.views import TCBase


class TestAdminAuth(TCBase):
    """
    관리자 계정 로그인을 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestAdminAuth, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/admin/auth'

    def setUp(self):
        super(TestAdminAuth, self).setUp()

        # ---

        self._request = lambda *, token=None, id=self.admin_id, pw=self.pw: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'id': id,
                'password': pw
            }
        )

    def _validate_response_data(self, resp):
        data = resp.json
        self.assertIsInstance(data, dict)

        self.assertIn('accessToken', data)
        self.assertIn('refreshToken', data)

        access_token = data['accessToken']
        refresh_token = data['refreshToken']

        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)

        self.assertRegex(access_token, self.token_regex)
        self.assertRegex(refresh_token, self.token_regex)

    def testAuthSuccess(self):
        # (1) 관리자 계정으로 로그인
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        self._validate_response_data(resp)

    def testAuthFailure_id(self):
        # (1) 존재하지 않는 ID로 로그인
        resp = self._request(id=self.student_id)

        # (2) status code 401
        self.assertEqual(resp.status_code, 401)

    def testAuthFailure_pw(self):
        # (1) 틀린 비밀번호로 로그인
        resp = self._request(pw='1')

        # (2) status code 401
        self.assertEqual(resp.status_code, 401)
