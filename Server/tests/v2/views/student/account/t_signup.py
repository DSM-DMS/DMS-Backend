from app.models.account import AdminModel, StudentModel, SignupWaitingModel

from tests.v2.views import TCBase


class TestStudentAccountSignup(TCBase):
    """
    학생 회원가입 테스트
    """
    def __init__(self, *args, **kwargs):
        super(TestStudentAccountSignup, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/auth'

        self.new_student_id = 'new_student'
        self.new_student_number = 2210
        self.new_student_name = 'student2'
        self.new_student_uuid = 'aaaa'

    def setUp(self):
        super(TestStudentAccountSignup, self).setUp()

        SignupWaitingModel(
            number=self.new_student_number,
            name=self.new_student_name,
            uuid=self.new_student_uuid
        ).save()

        self._request = lambda *, id=self.new_student_id, pw=self.pw, uuid=self.new_student_uuid: self.request(
            self.method,
            self.target_uri,
            json={
                'id': id,
                'password': pw,
                'uuid': uuid
            }
        )

        # ---

    def tearDown(self):
        StudentModel.objects(id=self.new_student_id).delete()
        SignupWaitingModel.objects(id=self.new_student_id).delete()

    def testSignupSuccess(self):
        # (1) 회원 가입
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) check database StudentModel
        student = StudentModel.objects(id=self.new_student_id)
        self.assertIsNotNone(student)

        self.assertEqual(student.name, self.new_student_name)
        self.assertEqual(student.number, self.new_student_number)

        # (4) check database SignupWaitingModel
        student = SignupWaitingModel.objects(uuid=self.new_student_uuid)
        self.assertIsNone(student)

    def testSignupFailure_idAlreadyExist(self):
        # (1) 회원가입
        resp = self._request(id=self.student_id)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

        # (3) check database StudentModel
        student = StudentModel.objects(number=self.new_student_number)
        self.assertIsNone(student)

        # (4) check database SignupWaitingModel
        student = SignupWaitingModel.objects(uuid=self.new_student_uuid)
        self.assertIsNotNone(student)

    def testSignupFailure_uuidDoesntExist(self):
        # (1) 회원가입
        resp = self._request(uuid='0000')

        # (2) status code 204
        self.assertEqual(resp.status_code, 205)

        # (3) check database StudentModel
        student = StudentModel.objects(number=self.new_student_number)
        self.assertIsNone(student)

        # (4) check database SignupWaitingModel
        student = SignupWaitingModel.objects(uuid=self.new_student_uuid)
        self.assertIsNotNone(student)