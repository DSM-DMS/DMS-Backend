from tests.views import TCBase


class TestAuth(TCBase):
    def testAuth(self):
        """
        TC about admin account authentication
        * This TC tests
        POST /admin/auth

        - Before Test
        None

        - Test
        Auth with id 'admin', pw 'pw'
        * Validation
        (1) status code : 200
        (2) response data type : dictionary
        (3) length of resource : 2
        (4) response data format
        {
            'access_token': str,
            'refresh_token': str
        }

        - Exception Test
        Auth with incorrect id or pw
        * Validation
        (1) status code : 401
        """
        # -- Test --
        resp = self.request(
            self.client.post,
            '/admin/auth',
            {'id': 'admin', 'pw': 'pw'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        data = self.get_response_data(resp)

        # (2)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 2)

        # (4)
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
            '/admin/auth',
            {'id': 'admin', 'pw': 'incorrect'},
            self.admin_access_token
        )
        # (1)
        self.assertEqual(resp.status_code, 401)
        # -- Exception Test --

    def testRefresh(self):
        """
        TC about admin access token refreshing
        * This TC tests
        POST /admin/refresh

        - Before Test
        None

        - Test
        Refresh with admin's refresh token
        * Validation
        (1) status code : 200
        (2) response data type : dictionary
        (3) length of resource : 1
        (4) response data format
        {
            'access_token': str
        }

        - Exception Test
        None
        """
        # -- Test --
        resp = self.request(
            self.client.post,
            '/admin/refresh',
            {},
            self.admin_refresh_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        data = self.get_response_data(resp)

        # (2)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
        self.assertIn('access_token', data)

        access_token = data['access_token']
        self.assertIsInstance(access_token, str)
        # -- Test --
