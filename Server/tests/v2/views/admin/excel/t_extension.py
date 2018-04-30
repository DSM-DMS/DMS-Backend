from tests.v2.views.admin.excel import ExcelTCBase


class TestExtensionExcelDownload(ExcelTCBase):
    """
    연장신청 정보 다운로드를 테스트합니다.
        * GET /admin/extension/11
        * GET /admin/extension/12
    """
    def test(self):
        self._test('/admin/extension/11')
        self._test('/admin/extension/12')
