SURVEY_GET = {
    'tags': ['설문지'],
    'description': '설문지 리스트 불러오기(학생 학년에 따라 필터링됨)',
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
                        'creation_time': '2017-12-26 13:58:50',
                        'title': '내일 저녁 치킨먹기 찬반설문',
                        'description': '설명!',
                        'start_date': '2017-10-24',
                        'end_date': '2017-10-25'
                    },
                    {
                        'id': '1fnfdj3391idkflds',
                        'creation_time': '2017-12-26 13:58:50',
                        'title': '등교 후 12시간 자습 찬반설문',
                        'description': '설명!',
                        'start_date': '2017-10-24',
                        'end_date': '2017-10-30'
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
            'name': 'survey_id',
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
                        'is_objective': True,
                        'choice_paper': ['예', '아니오'],
                        'answer': '예'
                    },
                    {
                        'id': '11265cd65432r9',
                        'title': '어디 치킨이 좋습니까?',
                        'is_objective': False,
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
    'description': '답변 남기기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'question_id',
            'description': '질문 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'answer',
            'description': '답변',
            'in': 'formData',
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
