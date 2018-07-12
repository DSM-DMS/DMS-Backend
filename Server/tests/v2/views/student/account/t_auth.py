from tests.v2.views import TCBase


class TestStudentAccountAuth(TCBase):
    """
    학생 계정 인증을 테스트 합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestStudentAccountAuth, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/auth'

    def setUp(self):
        super(TestStudentAccountAuth, self).setUp()

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

    def testAuthSuccess(self):
        # (1) 학생 계정으로 로그인
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        self.validate_auth_response(resp)

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
