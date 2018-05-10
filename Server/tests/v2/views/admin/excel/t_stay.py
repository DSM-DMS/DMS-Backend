from tests.v2.views.admin.excel import ExcelTCBase


class TestStayExcelDownload(ExcelTCBase):
    """
    잔류신청 정보 다운로드를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestStayExcelDownload, self).__init__('/admin/excel/stay', *args, **kwargs)

    def testDownloadSuccess(self):
        self._testDownloadSuccess()

    def testForbidden(self):
        self._testForbidden()
