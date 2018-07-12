from tests.v2.views import TCBase


class TestChangePassword(TCBase):
    """
    비밀번호 변경을 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestChangePassword, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/account/change-pw'

        self.new_pw = 'new'

    def setUp(self):
        super(TestChangePassword, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token, current_pw=self.pw, new_pw=self.new_pw: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'currentPassword': current_pw,
                'newPassword': new_pw
            }
        )

    def testPasswordChangeSuccess(self):
        # (1) 비밀번호 변경
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        self.student.reload()
        self.assertEqual(self.student.pw, self.encrypt_password(self.new_pw))

    def testPasswordChangeFailure_currentPasswordIncorrect(self):
        # (1) 틀린 현재 비밀번호로 비밀번호 변경
        resp = self._request(current_pw=self.pw + '12345')

        # (2) status code 403
        self.assertEqual(resp.status_code, 403)

    def testPasswordChangeFailure_currentPasswordAndNewPasswordIsEqual(self):
        # (1) 현재 비밀번호와 동일한 비밀번호를 새 비밀번호로 사용하여 변경
        resp = self._request(new_pw=self.pw)

        # (2) status code 409
        self.assertEqual(resp.status_code, 409)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.admin_access_token)
        self.assertEqual(resp.status_code, 403)
