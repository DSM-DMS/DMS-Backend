from app.models.version import VersionModel

from tests.v2.views import TCBase


class TestVersionUpload(TCBase):
    """
    버전 업로드를 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestVersionUpload, self).__init__(*args, **kwargs)

        self.method = self.client.put
        self.target_uri = '/metadata/version/{}'

        self.target_platform = 1
        self.new_version = '1.0'

    def setUp(self):
        super(TestVersionUpload, self).setUp()

        # ---

        self._request = lambda *, platform=self.target_platform, version=self.new_version: self.request(
            self.method,
            self.target_uri.format(platform),
            json={
                'version': version
            }
        )

    def testVersionUploadSuccess(self):
        # (1) 버전 업로드
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        version = VersionModel.objects(platform=self.target_platform).first()

        self.assertTrue(version)
        self.assertEqual(version.version, self.new_version)

    def testVersionUploadFailure_platformDoesNotExist(self):
        # (1) 수용하지 않는 platform id를 통해 버전 업로드
        resp = self._request(platform=0)

        # (2) status code 400
        self.assertEqual(resp.status_code, 400)


class TestVersionCheck(TCBase):
    """
    버전 체크를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestVersionCheck, self).__init__(*args, **kwargs)

        self.method = self.client.get
        self.target_uri = '/metadata/version/{}'

        self.platform = 1
        self.version = '1.0'

    def setUp(self):
        super(TestVersionCheck, self).setUp()

        # ---

        VersionModel(platform=self.platform, version=self.version).save()

        self._request = lambda *, platform=self.platform: self.request(
            self.method,
            self.target_uri.format(platform)
        )

    def testNewestVersionCheck(self):
        # (1) 최신 버전 체크
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) response data
        data = resp.json

        self.assertIn('version', data)
        self.assertEqual(data['version'], self.version)

    def testVersionCheckFailure_platformDoesNotExist(self):
        # (1) 버전 데이터가 존재하지 않는 플랫폼의 최신 버전 체크
        resp = self._request(platform=2)

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)
