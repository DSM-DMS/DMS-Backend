from flask_jwt_extended import create_refresh_token
from uuid import uuid4

from tests.v2.views import TCBase


class TestTokenRefresh(TCBase):
    """
    JWT 토큰 refresh를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestTokenRefresh, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/jwt/refresh'

    def setUp(self):
        super(TestTokenRefresh, self).setUp()

        # ---

        self._request = lambda *, token=self.admin_refresh_token: self.request(
            self.method,
            self.target_uri,
            token,
        )

    def testRefreshSuccess(self):
        # (1) Refresh
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        data = resp.json

        self.assertIn('accessToken', data)

        token = data['accessToken']
        self.assertIsInstance(token, str)
        self.assertRegex(token, self.token_regex)

    def testRefreshFailure_sentAccessToken(self):
        # (1) 액세스 토큰으로 refresh
        resp = self._request(token=self.student_access_token)

        # (2) status code 422
        self.assertEqual(resp.status_code, 422)

    def testRefreshFailure_tokenDoesNotExist(self):
        # (1) 존재하지 않는 refresh token으로 refresh
        with self.app.app_context():
            token = 'JWT {}'.format(create_refresh_token(str(uuid4())))

        resp = self._request(token=token)

        # (2) status code 401
        self.assertEqual(resp.status_code, 401)
