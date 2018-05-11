from app.models.post import FAQModel, NoticeModel, RuleModel

from tests.v2.views import TCBase

CATEGORY_MODEL_MAPPING = {
    'FAQ': FAQModel,
    'NOTICE': NoticeModel,
    'RULE': RuleModel
}


class TestPostUpload(TCBase):
    """
    게시글 업로드를 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestPostUpload, self).__init__(*args, **kwargs)

        self.method = self.client.post
        self.target_uri = '/admin/post/{}'

    def setUp(self):
        super(TestPostUpload, self).setUp()

        # ---

        self.title = '제목'
        self.content = '내용'

        self._request = lambda *, token=None, category='', title=self.title, content=self.content: self.request(
            self.method,
            self.target_uri.format(category),
            token,
            json={
                'title': self.title,
                'content': self.content
            }
        )

    def _testUploadSuccess(self, category):
        # (1) 업로드
        resp = self._request(category=category)

        # (2) status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) response data
        data = resp.json

        self.assertIn('id', data)

        id = data['id']
        self.assertIsInstance(id, str)

        # (4) 데이터베이스 확인
        posts = CATEGORY_MODEL_MAPPING[category.upper()].objects

        self.assertEqual(len(posts), 1)

        post = posts.first()

        self.assertEqual(str(post.id), id)
        self.assertEqual(post.title, self.title)
        self.assertEqual(post.content, self.content)

    def _testForbidden(self, category):
        resp = self._request(token=self.student_access_token, category=category)
        self.assertEqual(resp.status_code, 403)

    def testFAQ(self):
        self._testUploadSuccess('faq')
        self._testForbidden('faq')

    def testNotice(self):
        self._testUploadSuccess('notice')
        self._testForbidden('notice')

    def testRule(self):
        self._testUploadSuccess('rule')
        self._testForbidden('rule')


class TestPostPatch(TCBase):
    """
    게시글 수정을 테스트합니다.
    """
    def __init__(self, *args, **kwargs):
        super(TestPostPatch, self).__init__(*args, **kwargs)

        self.method = self.client.patch
        self.target_uri = '/admin/post/{}/{}'

    def setUp(self):
        super(TestPostPatch, self).setUp()

        # ---

        self.new_title = '새 제목'
        self.new_content = '새 내용'

        self._request = lambda *, token=None, category='', id='', title=self.new_title, content=self.new_content: self.request(
            self.method,
            self.target_uri.format(category, id or self.id),
            token,
            json={
                'title': self.new_title,
                'content': self.new_content
            }
        )

    def _post(self, category):
        resp = self.request(
            self.client.post,
            '/admin/post/{}'.format(category),
            json={
                'title': 'q',
                'content': 'q'
            }
        )

        self.id = resp.json['id']

    def _testPatchSuccess(self, category):
        # (1) 게시글 수정
        resp = self._request(category=category)

        # (2) status code 200
        self.assertEqual(resp.status_code, 200)

        # (3) 데이터베이스 확인
        post = CATEGORY_MODEL_MAPPING[category.upper()].objects(id=self.id).first()

        self.assertEqual(post.title, self.new_title)
        self.assertEqual(post.content, self.new_content)

    def _testPatchFailure_idDoesNotExist(self, category):
        # (1) 존재하지 않는 ID를 통해 게시글 수정
        resp = self._request(category=category, id='123')

        # (2) status code 204
        self.assertEqual(resp.status_code, 204)

    def _testForbidden(self, category):
        resp = self._request(token=self.student_access_token, category=category)
        self.assertEqual(resp.status_code, 403)

    def testFAQ(self):
        self._post('faq')
        self._testPatchSuccess('faq')
        self._testPatchFailure_idDoesNotExist('faq')
        self._testForbidden('faq')

    def testNotice(self):
        self._post('notice')
        self._testPatchSuccess('notice')
        self._testPatchFailure_idDoesNotExist('notice')
        self._testForbidden('notice')

    def testRule(self):
        self._post('rule')
        self._testPatchSuccess('rule')
        self._testPatchFailure_idDoesNotExist('rule')
        self._testForbidden('rule')

