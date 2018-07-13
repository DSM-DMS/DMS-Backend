from uuid import uuid4

from tests.v2.views import TCBase


class TestBugReport(TCBase):
    """
    버그신고를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestBugReport, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/student/report/bug'

        self.platform = 1
        self.content = str(uuid4())

    def setUp(self):
        super(TestBugReport, self).setUp()

        # ---

        self._request = lambda *, token=self.student_access_token, platform=self.platform, content=self.content: self.request(
            self.method,
            self.target_uri,
            token,
            json={
                'platform': platform,
                'content': content
            }
        )

    def testReportSuccess(self):
        # (1) 버그신고
        resp = self._request()

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

    def testForbidden(self):
        self.assertEqual(self._request(token=self.admin_access_token).status_code, 403)
