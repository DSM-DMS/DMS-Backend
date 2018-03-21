from app.models.post import FAQModel, NoticeModel, RuleModel

from tests.views import TCBase


class TestPostModify(TCBase):
    """
    TC about all of post modifications

    This TC tests
        * PATCH /admin/faq
        * PATCH /admin/notice
        * PATCH /admin/rule
    """
    def setUp(self):
        """
        - Before Test

        Upload posts
        Get post ids
            * POST /admin/faq
            * POST /admin/notice
            * POST /admin/rule
        """
        TCBase.setUp(self)

        # ---

        resp = self.request(
            self.client.post,
            '/admin/faq',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        self.faq_id = self.get_response_data(resp)['id']

        resp = self.request(
            self.client.post,
            '/admin/notice',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        self.notice_id = self.get_response_data(resp)['id']

        resp = self.request(
            self.client.post,
            '/admin/rule',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        self.rule_id = self.get_response_data(resp)['id']

    def tearDown(self):
        """
        - After Test
        """
        FAQModel.objects.delete()
        NoticeModel.objects.delete()
        RuleModel.objects.delete()

        # ---

        TCBase.tearDown(self)

    def _test(self, post_id, post_type):
        """
        - Test
        Modify post with post_id, post_type
            * Validation
            (1) status code : 200
            (2) load post with modified post id
                * Validation
                1. status code: 200
                2. response data type : dictionary
                3. length of resource : 5
                4. response data format
                {
                    'write_time': str(format: YYYY-MM-DD),
                    'author': 'fake_admin',
                    'title': 'title',
                    'content': 'content',
                    'pinned': False
                }

        :param post_id: post id for modify
        :type post_id: str

        :param post_type: faq or notice or rule
        :type post_type: str
        """
        # -- Test --
        resp = self.request(
            self.client.patch,
            '/admin/{}'.format(post_type),
            {'id': post_id, 'title': 'title_modified', 'content': 'content_modified'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        resp = self.request(
            self.client.get,
            '/{}/{}'.format(post_type, post_id)
        )

        # 1
        self.assertEqual(resp.status_code, 200)

        # 2
        data = self.get_response_data(resp)
        self.assertIsInstance(data, dict)

        # 3
        self.assertEqual(len(data), 5)

        # 4
        write_time = data['write_time']
        author = data['author']
        title = data['title']
        content = data['content']
        pinned = data['pinned']

        self.assertIsInstance(write_time, str)
        self.assertRegex(write_time, '\d\d\d\d-\d\d-\d\d')

        self.assertIsInstance(author, str)
        self.assertEqual(author, 'fake_admin')

        self.assertIsInstance(title, str)
        self.assertEqual(title, 'title_modified')

        self.assertIsInstance(content, str)
        self.assertEqual(content, 'content_modified')

        self.assertIsInstance(pinned, bool)
        self.assertFalse(pinned)
        # -- Test --

    def test(self):
        """
        - Test
        Modify FAQ, notice, rule with self._test()

        - Exception Test
        None
        """
        # -- Test --
        self._test(self.faq_id, 'faq')
        self._test(self.notice_id, 'notice')
        self._test(self.rule_id, 'rule')
        # -- Test --
