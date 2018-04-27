from tests.v2.views.admin.excel import ExcelTCBase


class TestGoingoutExcelDownload(ExcelTCBase):
    """
    외출신청 정보 다운로드를 테스트합니다.
        * GET /admin/goingout
    """
    def setUp(self):
        super(TestGoingoutExcelDownload, self).setUp()

    def tearDown(self):
        super(TestGoingoutExcelDownload, self).tearDown()

    def test(self):
        self._test('/admin/goingout')
