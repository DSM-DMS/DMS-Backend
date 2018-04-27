from tests.v2.views import TCBase


class TestStudentAccountControl(TCBase):
    """
    관리자의 학생 계정 제거를 테스트합니다.
        * DELETE /account-management/student
    """
    def setUp(self):
        super(TestStudentAccountControl, self).setUp()

        # ---

        self.delete = lambda number=self.student_number: self.json_request(
            self.client.delete,
            '/account-management/student',
            data={
                'number': number
            }
        )

        self.uuid_regex = '[0-9|a-f]{4}'

    def tearDown(self):
        super(TestStudentAccountControl, self).tearDown()

    def _validate_response_data(self, resp):
        data = self.get_response_data(resp)
        self.assertIn('uuid', data)

        uuid = data['uuid']
        self.assertIsInstance(uuid, str)

        self.assertRegex(uuid, self.uuid_regex)

    def test(self):
        # -- Test --
        # (1) 학생 계정 삭제
        resp = self.delete()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        self._validate_response_data(resp)

        # ---

        # (1) 이미 제거된 학생 계정 삭제
        resp = self.delete()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        self._validate_response_data(resp)

        # -- Test --

        # -- Exception Test --

        # (1) 존재하지 않는 학생 계정 삭제
        resp = self.delete(3119)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

        # -- Exception Test --


class TestAdminAccountCreation(TCBase):
    """
    관리자의 관리자 계정 생성을 테스트합니다.
        * POST /account-management/admin
    """
    def setUp(self):
        super(TestAdminAccountCreation, self).setUp()

        # ---

        self.new_admin_id = 'new_admin'

    def tearDown(self):
        super(TestAdminAccountCreation, self).tearDown()

    def test(self):
        # -- Test --

        # (1) 관리자 계정 생성
        resp = self.json_request(
            self.client.post,
            '/account-management/admin',
            data={
                'id': self.new_admin_id,
                'password': self.pw,
                'name': self.admin_name
            }
        )

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # -- Test --

        # -- Exception Test --

        # (1) 이미 존재하는 관리자 ID를 통해 계정 생성
        resp = self.delete(self.new_admin_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

        # -- Exception Test --


class TestAdminAccountDeletion(TCBase):
    """
    관리자의 관리자 계정 삭제를 테스트합니다.
        * DELETE /account-management/admin
    """
    def setUp(self):
        super(TestAdminAccountDeletion, self).setUp()

        # ---

        self.json_request(
            self.client.post,
            '/account-management/admin',
            data={
                'id': self.new_admin_id,
                'password': self.pw,
                'name': self.admin_name
            }
        )

        self.new_admin_id = 'new_admin'
        self.delete = lambda id=self.new_admin_id: self.json_request(
            self.client.delete,
            '/account-management/admin',
            data={
                'id': id
            }
        )

    def tearDown(self):
        super(TestAdminAccountDeletion, self).tearDown()

    def test(self):
        # -- Test --

        # (1) 관리자 계정 삭제
        resp = self.delete()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # -- Test --

        # -- Exception Test --

        # (1) 이미 삭제된 관리자 계정을 다시 삭제
        resp = self.delete()

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

        # ---

        # (1) 애초에 존재하지 않았던 관리자 계정 삭제
        resp = self.delete('1')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

        # -- Exception Test --
