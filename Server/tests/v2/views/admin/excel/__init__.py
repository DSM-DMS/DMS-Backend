from tests.v2.views import TCBase


class ExcelTCBase(TCBase):
    def setUp(self):
        super(ExcelTCBase, self).setUp()

        # ---

        self._request = lambda uri, *, token=None: self.request(
            self.client.get,
            uri,
            token
        )

    def _testDownloadSuccess(self, uri):
        # (1) 엑셀 다운로드
        resp = self._request(uri)

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response header
        self.assertIn('application / vnd.openxmlformats - officedocument.spreadsheetml.sheet', resp.headers)

    def _testForbidden(self, uri):
        # (1) 403 체크
        resp = self._request(uri, token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)

    def _test(self, uri):
        self._testDownloadSuccess(uri)
        self._testForbidden(uri)
