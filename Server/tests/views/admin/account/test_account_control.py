from tests.views import TCBase

from app.models.account import SignupWaitingModel


class TestAccountControl(TCBase):
    def tearDown(self):
        SignupWaitingModel.objects.delete()

        TCBase.tearDown(self)

    def testDeleteStudentAccount(self):
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
        (2) response data type : dictionary
        (3) length of resource : 1
        (4) response data format
        {
            'uuid': 'xxxx'(str)
        }

        - Exception Test
        Delete already initialized student account of number '1111'
        * Validation
        (1) status code : 201
        (2) response data type : dictionary
        (3) length of resource : 1
        (4) response data format
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

    def testDeleteAdminAccount(self):
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
            {'id': 'deleteme', 'pw': 'pw', 'name': 'test'},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 201)
        # -- Before Test --

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

    def testLoadStudentSignStatus(self):
        """
        TC about student's sign status loading
        * This TC tests
        GET /student-sign-status

        - Before Test
        None

        - Test
        Load student sign status
        * Validation
        (1) status code : 200
        (2) response data type : dictionary
        (3) length of resource : 2
        (4) response data format
        {
            'unsigned_student_count': int,
            'signed_student_count': int
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
