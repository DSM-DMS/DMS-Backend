from tests.v2.views import TCBase


class ExcelTCBase(TCBase):
    def __init__(self, target_uri, *args, **kwargs):
        super(ExcelTCBase, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = target_uri

    def setUp(self):
        super(ExcelTCBase, self).setUp()

        # ---

        self._request = lambda *, token=None: self.request(
            self.client.get,
            self.target_uri,
            token
        )

    def _testDownloadSuccess(self):
        # (1) 엑셀 다운로드
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response header
        self.assertIn('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', resp.headers.values())

    def _testForbidden(self):
        # (1) 403 체크
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)
