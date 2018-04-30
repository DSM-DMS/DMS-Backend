from app.models.account import AdminModel, StudentModel

from tests.v2.views import TCBase


class TestStudentAccountControl(TCBase):
    """
    관리자의 학생 계정 제거를 테스트합니다.
        * DELETE /account-management/student
    """
    def setUp(self):
        super(TestStudentAccountControl, self).setUp()

        # ---

        self._request = lambda *, token=None, number=self.student_number: self.request(
            self.client.delete,
            '/account-management/student',
            token,
            json={
                'number': number
            }
        )

        self.uuid_regex = '[0-9|a-f]{4}'

    def _validate_response_data(self, resp):
        data = self.get_response_data_as_json(resp)
        self.assertIsInstance(data, dict)

        self.assertIn('uuid', data)

        uuid = data['uuid']
        self.assertIsInstance(uuid, str)

        self.assertRegex(uuid, self.uuid_regex)

    def testDeletionSuccess(self):
        # (1) 학생 계정 삭제
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        self._validate_response_data(resp)

        # (4) 데이터베이스 확인
        self.assertFalse(StudentModel.objects)

    def testDeletionSuccess_alreadyDeleted(self):
        # (1) 이미 제거된 학생 계정 삭제
        self._request()
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self._validate_response_data(resp)

    def testDeletionFailure_numberDoesNotExist(self):
        # (1) 존재하지 않는 학생 계정 삭제
        resp = self._request(number=3119)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class TestAdminAccountCreation(TCBase):
    """
    관리자의 관리자 계정 생성을 테스트합니다.
        * POST /account-management/admin
    """
    def setUp(self):
        super(TestAdminAccountCreation, self).setUp()

        # ---

        self.new_admin_id = 'new_admin'

        self._request = lambda *, token=None, id=self.new_admin_id, pw=self.pw, name=self.admin_name: self.request(
            self.client.post,
            '/account-management/admin',
            token,
            json={
                'id': id,
                'password': pw,
                'name': name
            }
        )

    def testCreationSuccess(self):
        # (1) 관리자 계정 생성
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) 데이터베이스 확인
        admins = AdminModel.objects
        self.assertEqual(admins.count(), 2)

        admin = admins.filter(id=self.new_admin_id)
        self.assertTrue(admin)

    def testCreationFailure_alreadyExists(self):
        # (1) 이미 존재하는 관리자 ID를 통해 계정 생성
        resp = self._request(id=self.new_admin_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)


class TestAdminAccountDeletion(TCBase):
    """
    관리자의 관리자 계정 삭제를 테스트합니다.
        * DELETE /account-management/admin
    """
    def setUp(self):
        super(TestAdminAccountDeletion, self).setUp()

        # ---

        self.new_admin_id = 'new_admin'
        self.request(
            self.client.post,
            '/account-management/admin',
            json={
                'id': self.new_admin_id,
                'password': self.pw,
                'name': self.admin_name
            }
        )

        self._request = lambda *, token=None, id=self.new_admin_id: self.request(
            self.client.delete,
            '/account-management/admin',
            token,
            json={
                'id': id
            }
        )

    def testDeletionSuccess(self):
        # (1) 관리자 계정 삭제
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        new_admin = AdminModel.objects(id=self.new_admin_id)
        self.assertFalse(new_admin)

    def testDeletionFailure_alreadyDeleted(self):
        # (1) 이미 삭제된 관리자 계정을 다시 삭제
        self._request()
        resp = self._request()

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testDeletionFailure_idDoesNotExist(self):
        # (1) 애초에 존재하지 않았던 관리자 계정 삭제
        resp = self._request(id='1')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)
