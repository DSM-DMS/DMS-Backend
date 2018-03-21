from tests.views.admin.apply import ExcelDownloadTCBase


class TestGoingoutDownload(ExcelDownloadTCBase):
    """
    TC about goingout excel download

    This TC tests
        * GET /admin/goingout
    """
    def test(self):
        """
        - Test
        self.test_real()

        - Exception Test
        None
        """
        # -- Test --
        self._test('/admin/goingout')
        # -- Test --
