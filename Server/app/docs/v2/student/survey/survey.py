SURVEY_GET = {
    'tags': ['설문지'],
    'description': '''설문지 리스트 불러오기
    필터링 되는 설문조사
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
                'application/json': [
                    {
                        'id': 's3qldmc13opeflds',
                        'creationTime': '2018-04-15',
                        'title': '인상민 생일 선물 뭐 줄까?',
                        'description': '4월 20일은 인상민 생일인데 인상민한테 생일 선물 뭐 줄거예요?',
                        'startDate': '2018-04-15',
                        'endDate': '2018-04-20',
                        'answered': True
                    },
                    {
                        'id': '1fnfdj3391idkflds',
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
    'tags': ['설문지'],
    'description': '설문지 질문 리스트 불러오기',
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
                'application/json': [
                    {
                        'id': '13211265df16ads',
                        'title': '저녁에 치킨을 먹고 싶습니까?',
                        'isObjective': True,
                        'choicePaper': ['예', '아니오'],
                        'answer': '예'
                    },
                    {
                        'id': '11265cd65432r9',
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
    'tags': ['설문지'],
    'description': '질문에 대해 답변 남기기',
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
            'name': 'answer',
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
