from tests.views import TCBase

from app.models.post import FAQModel


class TestFAQ(TCBase):
    def tearDown(self):
        FAQModel.objects.delete()

        TCBase.tearDown(self)

    def testLoadFAQList(self):
        """
        TC about FAQ list inquiring
        * This TC tests
        GET /faq

        - Before Test
        Upload FAQ
        * POST /admin/faq

        - Test
        Load FAQ list
        * Validation
        (1) status code : 200
        (2) response data type : list
        (3) length of resource : 1
        (4) response data format
        [
            {
                'id': str(length: 24),
                'write_time': str(format: YYYY-MM-DD),
                'author': str(value: 'fake_admin'),
                'title': str(value: 'title'),
                'pinned': bool(value: False)
            },
            ...
        ]

        - Exception Test
        None
        """
        # -- Before Test --
        self.request(
            self.client.post,
            '/admin/faq',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        # -- Before Test --

        # -- Test --
        resp = self.request(
            self.client.get,
            '/faq'
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        data = self.get_response_data(resp)

        # (2)
        self.assertIsInstance(data, list)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
        faq = data[0]

        self.assertIn('id', faq)
        self.assertIn('write_time', faq)
        self.assertIn('author', faq)
        self.assertIn('title', faq)
        self.assertIn('pinned', faq)

        id = faq['id']
        write_time = faq['write_time']
        author = faq['author']
        title = faq['title']
        pinned = faq['pinned']

        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 24)

        self.assertIsInstance(write_time, str)
        self.assertRegex(write_time, '\d\d\d\d-\d\d-\d\d')

        self.assertIsInstance(author, str)
        self.assertEqual(author, 'fake_admin')

        self.assertIsInstance(title, str)
        self.assertEqual(title, 'title')

        self.assertIsInstance(pinned, bool)
        self.assertFalse(pinned)
        # -- Test --

    def testLoadFAQContent(self):
        """
        TC about FAQ content inquiring
        * This TC tests
        GET /faq/<post_id>

        - Before Test
        Upload FAQ
        Get uploaded FAQ ID
        * POST /admin/faq

        - Test
        Load FAQ content with uploaded FAQ ID
        * Validation
        (1) status code : 200
        (2) response data type : dict
        (3) length of resource : 5
        (4) response data format
        {
            'write_time': str(format: YYYY-MM-DD),
            'author': str(value: 'fake_admin'),
            'title': str(value: 'title'),
            'content': str(value: 'content'),
            'pinned': bool(value: False)
        }

        - Exception Test
        Load with nonexistent post id '1234'
        * Validation
        (1) status code : 204
        """
        # -- Before Test --
        resp = self.request(
            self.client.post,
            '/admin/faq',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )

        data = self.get_response_data(resp)
        id = data['id']
        # -- Before Test --

        # -- Test --
        resp = self.request(
            self.client.get,
            '/faq/{}'.format(id)
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        data = self.get_response_data(resp)

        # (2)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 5)

        # (4)
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
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.get,
            '/faq/{}'.format(1234)
        )

        # (1)
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --
