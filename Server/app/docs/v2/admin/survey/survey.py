from app.docs.v2 import SAMPLE_OBJECT_IDS

SURVEY_MANAGING_GET = {
    'tags': ['설문지 관리'],
    'description': '설문지 리스트를 불러옵니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '설문지 리스트 불러오기 성공',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'description': '치킨 어때?',
                        'creationTime': '2017-12-26',
                        'title': '내일 저녁 치킨먹기 찬반설문',
                        'startDate': '2017-10-24',
                        'endDate': '2017-10-25'
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'description': '졸리다',
                        'creationTime': '2017-12-26',
                        'title': '등교 후 12시간 자습 찬반설문',
                        'startDate': '2017-10-24',
                        'endDate': '2017-10-30'
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SURVEY_MANAGING_POST = {
    'tags': ['설문지 관리'],
    'description': '설문지를 등록합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'description',
            'description': '설문지 설명',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '설문지 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'startDate',
            'description': '시작 날짜(YYYY-MM-DD)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'endDate',
            'description': '종료 날짜(YYYY-MM-DD)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'target',
            'description': '대상 학년',
            'in': 'json',
            'type': 'list',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '설문지 등록에 성공했으며, 등록된 설문지의 ID를 응답합니다.',
            'examples': {
                'application/json': {
                    'id': SAMPLE_OBJECT_IDS[0]
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SURVEY_MANAGING_DELETE = {
    'tags': ['설문지 관리'],
    'description': '설문지를 삭제합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'surveyId',
            'description': '설문지 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '설문지 삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
