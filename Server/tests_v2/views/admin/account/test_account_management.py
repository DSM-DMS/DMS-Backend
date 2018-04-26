from tests_v2.views import TCBase

class TestStudentAccountControl(TCBase):
    """
    This TC tests
        * METHOD /
    """
    def setUp(self):
        super(TestStudentAccountControl, self).setUp()

        # ---

    def tearDown(self):
        # ---

        super(TestStudentAccountControl, self).tearDown()

    def test(self):
        # -- Test --

        # (1) Delete student account
        resp = self.json_request(
            self.client.delete,
            '/account-management/student',
            data={
                'number': self.student_number
            }
        )

        # (2) Check status code 201
        self.assertEqual(resp.status_code, 201)

        # (3) Check response data
        data = self.get_response_data(resp)
        self.assertIn('uuid', data)

        uuid = data['uuid']
        self.assertIsInstance(uuid, str)

        self.assertRegex(uuid, '[0-9|a-f]{4}')

        # (4)

        # ---

        # (1)
        # -- Test --

        # -- Exception Test --

        # (1)

        # (2)

        # (3)

        # (4)
        # -- Exception Test --