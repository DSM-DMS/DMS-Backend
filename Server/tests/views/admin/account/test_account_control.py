from tests.views import TCBase


class TestAccountControl(TCBase):
    def deleteStudentAccount(self):
        """
        TC about student account deletion

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
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --

    def deleteAdminAccount(self):
        """
        TC about admin account deletion

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
        # -- Before Test --

        # -- Test --
        # -- Test --

        # -- Exception Test --
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
