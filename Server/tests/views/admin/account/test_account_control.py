from tests.views import TCBase


class TestAccountControl(TCBase):
    def deleteStudentAccount(self):
        """
        TC about student account deletion
        * This TC tests
        POST /admin/account-control

        - Before Test
        None

        - Test
        Delete student account of number '1111'
        * Validation
        (1) status code : 201
        (2) length of resource : 1
        (3) response format(dictionary)
        {
            'uuid': 'xxxx'
        }

        - Exception Test
        Delete already initialized student account of number '1111'
        * Validation
        (1) status code : 201
        (2) length of resource : 1
        (3) response format(dictionary)
        {
            'uuid': 'xxxx'(str)
        }

        Delete student account of number '9999'
        * Validation
        (1) status code : 204
        """
        # -- Test --
        resp = self.request(
            self.client.post,
            '/admin/account-control',
            {'number': 1111},
            self.admin_access_token
        )

        self.assertEqual(resp.status_code, 201)

        data = self.get_response_data(resp)
        self.assertEqual(len(data), 1)
        self.assertIn('uuid', data)

        uuid = data['uuid']
        self.assertIsInstance(uuid, str)
        self.assertEqual(len(uuid), 4)
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.post,
            '/admin/account-control',
            {'number': 1111},
            self.admin_access_token
        )

        self.assertEqual(resp.status_code, 201)

        data = self.get_response_data(resp)
        self.assertEqual(len(data), 1)
        self.assertIn('uuid', data)

        uuid = data['uuid']
        self.assertIsInstance(uuid, str)
        self.assertEqual(len(uuid), 4)

        # ---

        resp = self.request(
            self.client.post,
            '/admin/account-control',
            {'number': 9999},
            self.admin_access_token
        )

        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --

    def deleteAdminAccount(self):
        """
        TC about admin account deletion
        * This TC tests
        DELETE /admin/account-control

        - Before Test
        Create new admin account of id 'deleteme'
        * POST /admin/new-account

        - Test
        Delete admin account of id 'deleteme'
        * Validation
        (1) status code : 200

        - Exception Test
        Delete already deleted admin account of id 'deleteme'
        * Validation
        (1) status code : 204
        """
        # -- Before Test --
        resp = self.request(
            self.client.post,
            '/admin/new-account',
            {'id': 'deleteme', 'pw': 'pw'},
            self.admin_access_token
        )
        self.assertEqual(resp.status_code, 201)
        # -- Before Test --

        # -- Test --
        resp = self.request(
            self.client.delete,
            '/admin/account-control',
            {'id': 'deleteme'},
            self.admin_access_token
        )
        self.assertEqual(resp.status_code, 200)
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.delete,
            '/admin/account-control',
            {'id': 'deleteme'},
            self.admin_access_token
        )
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --

    def loadStudentSignStatus(self):
        """
        TC about student's sign status loading

        - Before Test
        None

        - Test
        Load student sign status
        * Validation
        (1) status code : 200
        (2) length of resource : 2
        (3) response format(dictionary)
        {
            'unsigned_student_count': int,
            'signed_student_count': int
        }

        - Exception Test
        None
        """
        # -- Test --
        # -- Test --
