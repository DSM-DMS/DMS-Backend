from app.docs.v2 import SAMPLE_OBJECT_IDS

QUESTION_MANAGING_GET = {
    'tags': ['[Admin] 설문지 관리'],
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
            'description': '질문 리스트 불러오기 성공',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'title': '저녁에 치킨을 먹고 싶습니까?',
                        'isObjective': True,
                        'choicePaper': ['예', '아니오']
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'title': '어디 치킨이 좋습니까?',
                        'isObjective': False
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

QUESTION_MANAGING_POST = {
    'tags': ['[Admin] 설문지 관리'],
    'description': '설문지에 1개 이상의 질문을 등록합니다. 각 질문 데이터(title, isObjective, choicePaper)는 "questions"에 array로 묶어 전송합니다.',
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
            'description': '질문을 추가할 설문지 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '질문 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'isObjective',
            'description': '객관식 여부',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'choicePaper',
            'description': '객관식 선택지',
            'in': 'json',
            'type': 'list',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '질문 추가에 성공하였으며, 업로드된 질문의 ID를 응답합니다.',
            'examples': {
                '': SAMPLE_OBJECT_IDS
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
