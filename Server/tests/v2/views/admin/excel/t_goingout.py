from tests.v2.views.admin.excel import ExcelTCBase


class TestGoingoutExcelDownload(ExcelTCBase):
    """
    외출신청 정보 다운로드를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestGoingoutExcelDownload, self).__init__('/admin/excel/goingout', *args, **kwargs)
    
    def testDownloadSuccess(self):
        self._testDownloadSuccess()

    def testForbidden(self):
        self._testForbidden()
