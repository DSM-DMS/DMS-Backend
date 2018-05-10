from datetime import datetime

from app.models.account import StudentModel
from app.models.point import PointHistoryModel

from tests.v2.views import TCBase


class TestStudentList(TCBase):
    """
    학생 리스트 조회를 테스트합니다.
        * GET /admin/point/student
    """
    def setUp(self):
        super(TestStudentList, self).setUp()

        # ---

        self.student.point_histories.append(
            PointHistoryModel(
                reason='상점 규칙',
                point_type=True,
                point=1
            )
        )

        self.student.good_point += 1

        self.now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.student.save()

        self._request = lambda *, token=None: self.request(
            self.client.get,
            '/admin/point/student',
            token
        )

    def testInquireSuccess(self):
        # (1) 학생 리스트 조회
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        data = resp.json

        self.assertListEqual(data, [
            {
                'id': self.student_id,
                'name': self.student_name,
                'number': self.student_number,
                'goodPoint': 1,
                'badPoint': 0,
                'penaltyLevel': 0,
                'pointHistories': [
                    {
                        'time': self.now,
                        'reason': '상점 규칙',
                        'pointType': True,
                        'point': 1
                    }
                ],
                'penaltyTrainingStatus': 0
            }
        ])

    def testForbidden(self):
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)

