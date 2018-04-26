from tests.v1.views.admin.apply import ExcelDownloadTCBase


class TestExtension11Download(ExcelDownloadTCBase):
    """
    TC about extension 11 excel download

    This TC tests
        * GET /admin/extension/11
    """
    def test(self):
        """
        - Test
        self.test_real()

        - Exception Test
        None
        """
        # -- Test --
        self._test('/admin/extension/11')
        # -- Test --


class TestExtension12Download(ExcelDownloadTCBase):
    """
    TC about extension 12 excel download

    This TC tests
        * GET /admin/extension/12
    """
    def test(self):
        """
        - Test
        self.test_real()

        - Exception Test
        None
        """
        # -- Test --
        self._test('/admin/extension/12')
        # -- Test --
