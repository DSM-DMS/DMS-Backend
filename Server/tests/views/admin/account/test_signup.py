from tests.views import TCBase


class TestNewAdminAccount(TCBase):
    """
    TC about admin account creation

    This TC tests
        * POST /admin/new-account
    """
    def setUp(self):
        """
        - Before Test
        """
        TCBase.setUp(self)

    def tearDown(self):
        """
        - After Test
        """
        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Create new admin account with id 'admin-new', pw 'pw'
            * Validation
            (1) status code : 201
            (2) auth with created admin account
                * Validation
                1. status code: 200
                2. response data type : dictionary
                3. length of resource : 2
                4. response data format
                {
                    'access_token': str,
                    'refresh_token': str
                }

        - Exception Test
        Create new admin account with already existing id 'admin-new'
            * Validation
            (1) status code : 204
        """
        # -- Test --
        resp = self.request(
            self.client.post,
            '/admin/new-account',
            {'id': 'admin-new', 'pw': 'pw', 'name': 'test'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 201)

        # (2)
        resp = self.request(
            self.client.post,
            '/admin/auth',
            {'id': 'admin', 'pw': 'pw'},
            self.admin_access_token
        )

        # 1
        self.assertEqual(resp.status_code, 200)

        # 2
        data = self.get_response_data(resp)
        self.assertIsInstance(data, dict)

        # 3
        self.assertEqual(len(data), 2)

        # 4
        self.assertIn('access_token', data)
        self.assertIn('refresh_token', data)

        access_token = data['access_token']
        refresh_token = data['refresh_token']

        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.post,
            '/admin/new-account',
            {'id': 'admin-new', 'pw': 'pw', 'name': 'test'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --
