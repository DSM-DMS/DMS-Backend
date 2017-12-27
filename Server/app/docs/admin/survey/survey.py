SURVEY_POST = {
    'tags': ['설문조사 관리'],
    'description': '설문지 등록',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '설문지 제목',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'start_date',
            'description': '시작 날짜(YYYY-MM-DD)',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'end_date',
            'description': '종료 날짜(YYYY-MM-DD)',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'target',
            'description': '대상 학년',
            'in': 'formData',
            'type': 'list',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '설문지 등록 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

QUESTION_POST = {
    'tags': ['설문조사 관리'],
    'description': '설문지에 질문 등록',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '질문을 추가할 설문지 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '질문 제목',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'is_objective',
            'description': '객관식 여부',
            'in': 'formData',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'choice_paper',
            'description': '객관식 선택지',
            'in': 'formData',
            'type': 'list',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '질문 추가 성공'
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
