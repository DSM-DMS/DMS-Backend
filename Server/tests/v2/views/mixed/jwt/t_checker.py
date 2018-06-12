from flask_jwt_extended import create_access_token

from tests.v2.views import TCBase


class TestAuthChecker(TCBase):
    """
    Access Token의 유효성 체크를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestAuthChecker, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/jwt/check'

    def setUp(self):
        super(TestAuthChecker, self).setUp()

        # ---

        self._request = lambda *, token=None: self.request(
            self.method,
            self.target_uri,
            token
        )

    def testCheckSuccess(self):
        # (1) JWT check
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

    def testCheckFailure_unknownIdentity(self):
        # (1) UUID 형태가 아닌 identity로 구성된 토큰
        with self.app.app_context():
            token = 'JWT {}'.format(create_access_token('123'))

        resp = self._request(token=token)

        # (2) status code 401
        self.assertEqual(resp.status_code, 422)
