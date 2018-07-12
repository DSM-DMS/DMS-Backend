from app.models.account import AdminModel, StudentModel, SignupWaitingModel

from tests.v2.views import TCBase


class TestStudentAccountSignup(TCBase):
    """
    학생 회원가입을 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestStudentAccountSignup, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/signup'

    def setUp(self):
        super(TestStudentAccountSignup, self).setUp()

        # ---

        self.new_student_data = {
            'uuid': 'aaaa',
            'id': 'new_student',
            'pw': self.pw,
            'name': 'DMS',
            'number': 1111
        }

        SignupWaitingModel(
            uuid=self.new_student_data['uuid'],
            name=self.new_student_data['name'],
            number=self.new_student_data['number']
        ).save()

        self._request = lambda *, uuid=self.new_student_data['uuid'], id=self.new_student_data['id'], pw=self.new_student_data['pw']: self.request(
            self.method,
            self.target_uri,
            json={
                'uuid': uuid,
                'id': id,
                'password': pw
            }
        )

    def testSignupSuccess(self):
        # (1) 회원가입
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) 데이터베이스 확인
        student = StudentModel.objects(
            id=self.new_student_data['id'],
            pw=self.encrypt_password(self.new_student_data['pw']),
            name=self.new_student_data['name'],
            number=self.new_student_data['number']
        ).first()
        # 조건을 고의적으로 많이 달아서, 별도의 assertion 코드를 줄임

        self.assertTrue(student)

        self.assertFalse(SignupWaitingModel.objects(uuid=self.new_student_data['uuid']))

    def testSignupFailure_idAlreadyExist(self):
        # (1) 회원가입
        resp = self._request(id=self.student_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 409)

    def testSignupFailure_uuidDoesntExist(self):
        # (1) 회원가입
        resp = self._request(uuid=self.new_student_data['uuid'] + '12345')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)
