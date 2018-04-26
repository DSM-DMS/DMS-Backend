import ujson

from tests_v1.views import TCBase

from app.models.survey import SurveyModel


class TestSurveyLoad(TCBase):
    """
    TC about survey list inquiring

    This TC tests_v1
        * GET /admin/survey
    """
    def setUp(self):
        """
        - Before Test

        Upload survey
            * POST /admin/survey

        Upload question for API's business logic
            * POST /admin/survey/question
        """
        TCBase.setUp(self)

        # ---

        resp = self.request(
            self.client.post,
            '/admin/survey',
            {
                'title': 'title',
                'description': 'description',
                'start_date': '2018-01-01',
                'end_date': '2018-03-01',
                'target': ujson.dumps([1, 3])
            },
            self.admin_access_token
        )

        survey_id = self.get_response_data(resp)['id']

        self.json_request(
            self.client.post,
            '/admin/survey/question',
            {
                'survey_id': survey_id,
                'questions': [
                    {
                        'title': 'title',
                        'is_objective': False
                    },
                    {
                        'title': 'title',
                        'is_objective': False
                    }
                ]
            },
            self.admin_access_token
        )

    def tearDown(self):
        """
        - After Test
        """
        SurveyModel.objects.delete()

        # ---

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Load surveys
            * Validation
            (1) status code : 200
            (2) response data type : list
            (3) length of resource : 1
            (4) response data format
            {
                'id': str(length: 24),
                'creation_time': str(format: YYYY-MM-DD),
                'title': 'title',
                'description': 'description',
                'start_date': '2018-01-01',
                'end_date': '2018-03-01'
            }

        - Exception Test
        None
        """
        # -- Test --
        resp = self.request(
            self.client.get,
            '/admin/survey',
            {},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        data = self.get_response_data(resp)
        self.assertIsInstance(data, list)

        # (3)
        self.assertEqual(len(data), 1)

        # (4)
        survey = data[0]

        self.assertIn('id', survey)
        id = survey['id']
        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 24)

        self.assertIn('creation_time', survey)
        creation_time = survey['creation_time']
        self.assertIsInstance(creation_time, str)
        self.assertRegex(creation_time, '\d\d\d\d-\d\d-\d\d')

        del survey['id'], survey['creation_time']

        self.assertDictEqual(survey, {
            'title': 'title',
            'description': 'description',
            'start_date': '2018-01-01',
            'end_date': '2018-03-01'
        })
        # -- Test --


class Test(TCBase):
    """
    TC about survey uploading

    This TC tests_v1
        * POST /admin/survey
    """
    def setUp(self):
        """
        - Before Test
        """
        TCBase.setUp(self)

        # ---

    def tearDown(self):
        """
        - After Test
        """
        # ---

        TCBase.tearDown(self)

    def test(self):
        """
        - Test
        Upload survey
            * Validation
            (1) status code : 1
            (2) response data type : dictionary
            (3) length of resource : 1
            (4) response data format
            {
                
            }
        """
        # -- Test --

        # (1)

        # (2)

        # (3)

        # (4)
        # -- Test --
