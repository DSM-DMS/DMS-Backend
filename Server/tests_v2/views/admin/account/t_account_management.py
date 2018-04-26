from tests_v2.views import TCBase


class TestStudentAccountControl(TCBase):
    """
    관리자의 학생 계정 제거를 테스트합니다.
        * DELETE /account-management/student
    """
    def setUp(self):
        super(TestStudentAccountControl, self).setUp()

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
