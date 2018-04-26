from tests.v1.views import TCBase


class ExcelDownloadTCBase(TCBase):
    def _test(self, uri):
        """
        - Test
        Download excel file with served uri
            * Validation
            (1) status code : 200
            (2) response data type : application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
        """
        resp = self.request(
            self.client.get,
            uri,
            {},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        self.assertEqual(resp.content_type, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
