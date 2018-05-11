from app.models.post import FAQModel, NoticeModel, RuleModel

from tests.v2.views import TCBase

CATEGORY_MODEL_MAPPING = {
    'FAQ': FAQModel,
    'NOTICE': NoticeModel,
    'RULE': RuleModel
}


class TestPreviewSetting(TCBase):
    """
    관리자의 게시글 프리뷰 설정을 테스트합니다.
    """

    def __init__(self, *args, **kwargs):
        super(TestPreviewSetting, self).__init__(*args, **kwargs)

        self.method = self.client.patch
        self.target_uri = '/admin/post-preview/{}'

    def setUp(self):
        super(TestPreviewSetting, self).setUp()

        # ---

        self._request = lambda *, token=None, id='': self.request(
            self.method,
            self.target_uri.format(self.category),
            token,
            json={
                'id': id or self.id
            }
        )

    def _post(self):
        resp = self.request(
            self.client.post,
            '/admin/post/{}'.format(self.category),
            json={
                'title': 'q',
                'content': 'q'
            }
        )

        self.id = resp.json['id']

    def _testPatchSuccess(self):
        # (1) 게시글 프리뷰 설정
        resp = self._request()

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        post = CATEGORY_MODEL_MAPPING[self.category.upper()].objects(pinned=True).first()

        self.assertEqual(self.id, str(post.id))

    def _testPatchFailure_idDoesNotExist(self):
        # (1) 존재하지 않는 게시글 ID를 이용해 프리뷰 설정
        resp = self._request(id='123')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def _testForbidden(self):
        resp = self._request(token=self.student_access_token)
        self.assertEqual(resp.status_code, 403)

    def testFAQ(self):
        self.category = 'faq'
        self._post()
        self._post()
        self._testPatchSuccess()
        self._testPatchFailure_idDoesNotExist()
        self._testForbidden()

    def testNotice(self):
        self.category = 'notice'
        self._post()
        self._post()
        self._testPatchSuccess()
        self._testPatchFailure_idDoesNotExist()
        self._testForbidden()

    def testRule(self):
        self.category = 'rule'
        self._post()
        self._post()
        self._testPatchSuccess()
        self._testPatchFailure_idDoesNotExist()
        self._testForbidden()
