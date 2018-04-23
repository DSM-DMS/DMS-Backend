from app.docs.v2 import SAMPLE_OBJECT_IDS

SURVEY_GET = {
    'tags': ['[Student] 설문 조사'],
    'description': '''설문지 리스트를 불러옵니다.
    아래의 조건 중 하나 이상에 맞는 설문조사는 response되지 않습니다.
    
    1. 대상이 해당 학년이 아닌 설문조사
    2. 설문 기간이 지난 설문조사
    3. 질문이 없는 설문조사
    ''',
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
                        'creationTime': '2018-04-15',
                        'title': '인상민 생일 선물 뭐 줄까?',
                        'description': '4월 20일은 인상민 생일인데 인상민한테 생일 선물 뭐 줄거예요?',
                        'startDate': '2018-04-15',
                        'endDate': '2018-04-20',
                        'answered': True
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'creationTime': '2018-03-02',
                        'title': '아침운동 시행 찬반 설문조사',
                        'description': '설명!',
                        'startDate': '2018-03-02',
                        'endDate': '2018-12-31',
                        'answered': False
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

QUESTION_GET = {
    'tags': ['[Student] 설문 조사'],
    'description': '설문지 질문 리스트를 불러옵니다.',
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
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '질문 리스트 불러오기 성공. 답변했다면 답변도 함께 반환됩니다.',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'title': '저녁에 치킨을 먹고 싶습니까?',
                        'isObjective': True,
                        'choicePaper': ['예', '아니오'],
                        'answer': '예'
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'title': '어디 치킨이 좋습니까?',
                        'isObjective': False,
                        'answer': None
                    }
                ]
            }
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

QUESTION_POST = {
    'tags': ['[Student] 설문 조사'],
    'description': '질문에 답변을 남깁니다. 이미 답변을 남겼을 경우, 덮어씌웁니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'questionId',
            'description': '질문 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'answerContent',
            'description': '답변',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '답변 남기기 성공'
        },
        '204': {
            'description': '존재하지 않는 질문 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
