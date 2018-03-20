from tests.views import TCBase

from app.models.account import SignupWaitingModel


class TestDeleteStudentAccount(TCBase):
    """
    TC about student account deletion

    * This TC tests
        POST /admin/account-control
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
        SignupWaitingModel.objects.delete()

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Delete student account of number '1111'
            * Validation
            (1) status code : 201
            (2) response data type : dictionary
            (3) length of resource : 1
            (4) response data format
            {
                'uuid': str(length: 4)
            }

        - Exception Test
        Delete already initialized student account of number '1111'
            * Validation
            (1) status code : 201
            (2) response data type : dictionary
            (3) length of resource : 1
            (4) response data format
            {
                'uuid': str(length: 4)
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

        # (1)
        self.assertEqual(resp.status_code, 201)

        data = self.get_response_data(resp)

        # (2)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
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

        # (1)
        self.assertEqual(resp.status_code, 201)

        data = self.get_response_data(resp)

        # (2)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
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

        # (1)
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --


class TestDeleteAdminAccount(TCBase):
    """
    TC about admin account deletion

    This TC tests
        * DELETE /admin/account-control
    """
    def setUp(self):
        """
        - Before Test

        Create new admin account of id 'deleteme'
            * POST /admin/new-account
        """
        TCBase.setUp(self)

        self.request(
            self.client.post,
            '/admin/new-account',
            {'id': 'deleteme', 'pw': 'pw', 'name': 'test'},
            self.admin_access_token
        )

    def tearDown(self):
        """
        - After Test
        """
        SignupWaitingModel.objects.delete()

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Delete admin account of id 'deleteme'
            * Validation
            (1) status code : 200

        - Exception Test
        Delete already deleted admin account of id 'deleteme'
            * Validation
            (1) status code : 204
        """
        # -- Test --
        resp = self.request(
            self.client.delete,
            '/admin/account-control',
            {'id': 'deleteme'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.delete,
            '/admin/account-control',
            {'id': 'deleteme'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --


class TestLoadStudentSignStatus(TCBase):
    """
    TC about student's sign status loading

    This TC tests
        * GET /student-sign-status
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
        SignupWaitingModel.objects.delete()

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Load student sign status
            * Validation
            (1) status code : 200
            (2) response data type : dictionary
            (3) length of resource : 2
            (4) response data format
            {
                'unsigned_student_count': int(value: 0),
                'signed_student_count': int(value: 1)
            }

        - Exception Test
        None
        """
        # -- Test --
        resp = self.request(
            self.client.get,
            '/admin/student-sign-status',
            {},
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
        self.assertIn('unsigned_student_count', data)
        self.assertIn('signed_student_count', data)

        unsigned_student_count = data['unsigned_student_count']
        signed_student_count = data['signed_student_count']

        self.assertIsInstance(unsigned_student_count, int)
        self.assertIsInstance(signed_student_count, int)

        self.assertEqual(unsigned_student_count, 0)
        self.assertEqual(signed_student_count, 1)
        # -- Test --
