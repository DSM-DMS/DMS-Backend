from tests_v1.views import TCBase

from app_v1.models.account import SignupWaitingModel


class TestDeleteStudentAccount(TCBase):
    """
    TC about student account deletion

    * This TC tests_v1
        POST /admin/account-control
    """
    def tearDown(self):
        """
        - After Test
        """
        SignupWaitingModel.objects.delete()

        # ---

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

        # (2)
        data = self.get_response_data(resp)
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

        # (2)
        data = self.get_response_data(resp)
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

    This TC tests_v1
        * DELETE /admin/account-control
    """
    def setUp(self):
        """
        - Before Test

        Create new admin account of id 'deleteme'
            * POST /admin/new-account
        """
        TCBase.setUp(self)

        # ---

        self.id_for_delete = 'deleteme'

        self.request(
            self.client.post,
            '/admin/new-account',
            {'id': self.id_for_delete, 'pw': 'pw', 'name': 'test'},
            self.admin_access_token
        )

    def tearDown(self):
        """
        - After Test
        """
        SignupWaitingModel.objects.delete()

        # ---

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
            {'id': self.id_for_delete},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)
        # -- Test --

        # -- Exception Test --
        resp = self.request(
            self.client.delete,
            '/admin/account-control',
            {'id': self.id_for_delete},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 204)
        # -- Exception Test --


class TestLoadStudentSignStatus(TCBase):
    """
    TC about student's sign status loading

    This TC tests_v1
        * GET /student-sign-status
    """
    def tearDown(self):
        """
        - After Test
        """
        SignupWaitingModel.objects.delete()

        # ---

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
                'unsigned_student_count': 0,
                'signed_student_count': 1
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

        # (2)
        data = self.get_response_data(resp)
        self.assertIsInstance(data, dict)

        # (3)
        self.assertEqual(len(data), 2)

        # (4)
        self.assertDictEqual(data, {
            'unsigned_student_count': 0,
            'signed_student_count': 1
        })
        # -- Test --
