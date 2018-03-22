from app.models.post import FAQModel, NoticeModel, RuleModel

from tests.views import TCBase


class TestPostUpload(TCBase):
    """
    TC about all of post uploads

    This TC tests
        * POST /admin/faq
        * POST /admin/notice
        * POST /admin/rule
    """
    def tearDown(self):
        """
        - After Test
        """
        FAQModel.objects.delete()
        NoticeModel.objects.delete()
        RuleModel.objects.delete()

        # ---

        TCBase.tearDown(self)

    def _test(self, post_type):
        """
        - Test
        Upload post with served post_type
            * Validation
            (1) status code : 201
            (2) response data type : dictionary
            (3) length of resource : 1
            (4) response data format
            {
                'id': str(length: 24)
            }
            (5) load post with created post id
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

        :param post_type: faq or notice or rule
        :type post_type: str
        """
        resp = self.request(
            self.client.post,
            '/admin/{}'.format(post_type),
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 201)

        # (2)
        data = self.get_response_data(resp)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
        self.assertIn('id', data)

        id = data['id']

        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 24)

        # (5)
        resp = self.request(
            self.client.get,
            '/{}/{}'.format(post_type, id)
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
        self.assertEqual(title, 'title')

        self.assertIsInstance(content, str)
        self.assertEqual(content, 'content')

        self.assertIsInstance(pinned, bool)
        self.assertFalse(pinned)

    def test(self):
        """
        - Test
        Upload FAQ, notice, rule with self._test()

        - Exception Test
        None
        """
        # -- Test --
        self._test('faq')
        self._test('notice')
        self._test('rule')
        # -- Test --