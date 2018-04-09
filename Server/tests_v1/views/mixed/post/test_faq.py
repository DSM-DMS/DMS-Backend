from tests_v1.views import TCBase

from app_v2.models.post import FAQModel


class TestLoadFAQList(TCBase):
    """
    TC about FAQ list inquiring

    This TC tests_v1
        * GET /faq
    """
    def setUp(self):
        """
        - Before Test

        Upload FAQ
            * POST /admin/faq
        """
        TCBase.setUp(self)

        self.faq = {
            'title': 'title',
            'content': 'content'
        }

        self.request(
            self.client.post,
            '/admin/faq',
            self.faq,
            self.admin_access_token
        )

    def tearDown(self):
        """
        - After Test
        """
        FAQModel.objects.delete()

        TCBase.tearDown(self)

    def test(self):
        """
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
                    'author': 'fake_admin',
                    'title': 'title',
                    'pinned': False
                },
                ...
            ]

        - Exception Test
        None
        """
        # -- Test --
        resp = self.request(
            self.client.get,
            '/faq'
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        data = self.get_response_data(resp)
        self.assertIsInstance(data, list)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
        faq = data[0]

        self.assertIn('id', faq)
        self.assertIn('write_time', faq)

        id = faq['id']
        write_time = faq['write_time']

        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 24)

        self.assertIsInstance(write_time, str)
        self.assertRegex(write_time, '\d\d\d\d-\d\d-\d\d')

        del faq['id'], faq['write_time']

        self.faq.update({'author': 'fake_admin', 'pinned': False})
        del self.faq['content']
        self.assertDictEqual(faq, self.faq)
        # -- Test --


class TestLoadFAQContent(TCBase):
    """
    TC about FAQ content inquiring

    * This TC tests_v1
        GET /faq/<post_id>
    """

    def setUp(self):
        """
        - Before Test

        Upload FAQ
        Get uploaded FAQ ID
        * POST /admin/faq
        """
        TCBase.setUp(self)

        # ---

        self.faq = {
            'title': 'title',
            'content': 'content'
        }

        resp = self.request(
            self.client.post,
            '/admin/faq',
            self.faq,
            self.admin_access_token
        )

        data = self.get_response_data(resp)
        self.id = data['id']

    def tearDown(self):
        """
        - After Test
        """
        FAQModel.objects.delete()

        # ---

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Load FAQ content with uploaded FAQ ID
            * Validation
            (1) status code : 200
            (2) response data type : dictionary
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
        # -- Test --
        resp = self.request(
            self.client.get,
            '/faq/{}'.format(self.id)
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        data = self.get_response_data(resp)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 5)

        # (4)
        self.assertIn('write_time', data)
        write_time = data['write_time']
        self.assertIsInstance(write_time, str)
        self.assertRegex(write_time, '\d\d\d\d-\d\d-\d\d')

        del data['write_time']

        self.faq.update({'author': 'fake_admin', 'pinned': False})
        self.assertDictEqual(data, self.faq)
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.get,
            '/faq/{}'.format(1234)
        )

        # (1)
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --
