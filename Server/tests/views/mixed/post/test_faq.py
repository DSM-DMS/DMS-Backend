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

