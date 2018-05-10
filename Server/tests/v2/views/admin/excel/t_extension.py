from tests.v2.views.admin.excel import ExcelTCBase


class TestExtension11ExcelDownload(ExcelTCBase):
    """
    11시 연장신청 정보 다운로드를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestExtension11ExcelDownload, self).__init__('/admin/excel/extension/11', *args, **kwargs)

    def testDownloadSuccess(self):
        self._testDownloadSuccess()

    def testForbidden(self):
        self._testForbidden()


class TestExtension12ExcelDownload(ExcelTCBase):
    """
    12시 연장신청 정보 다운로드를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestExtension12ExcelDownload, self).__init__('/admin/excel/extension/12', *args, **kwargs)

    def testDownloadSuccess(self):
        self._testDownloadSuccess()

    def testForbidden(self):
        self._testForbidden()
