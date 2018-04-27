from tests.v2.views.admin.excel import ExcelTCBase


class TestStayExcelDownload(ExcelTCBase):
    """
    잔류신청 정보 다운로드를 테스트합니다.
        * GET /admin/stay
    """
    def setUp(self):
        super(TestStayExcelDownload, self).setUp()

    def tearDown(self):
        super(TestStayExcelDownload, self).tearDown()

    def test(self):
        self._test('/admin/stay')
