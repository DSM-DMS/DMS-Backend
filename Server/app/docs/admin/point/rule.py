POINT_RULE_MANAGING_GET = {
    'tags': ['상벌점 관리'],
    'description': '상벌점 규칙 목록 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '목록 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'id': '2316ca13cb1a',
                        'name': '치킨이 맛있는 규칙',
                        'min_point': 1,
                        'max_point': 3
                    },
                    {
                        'id': '2316ca13cb1b',
                        'name': '저녁에 배고픈 규칙',
                        'min_point': -1,
                        'max_point': -3
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POINT_RULE_MANAGING_POST = {
    'tags': ['상벌점 관리'],
    'description': '상벌점 규칙 추가',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '상벌점 규칙의 이름',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'min_point',
            'description': '최소 점수',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
        {
            'name': 'max_point',
            'description': '최대 점수',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '상벌점 데이터 등록 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POINT_RULE_MANAGING_PATCH = {
    'tags': ['상벌점 관리'],
    'description': '상벌점 규칙 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'rule_id',
            'description': '수정할 상벌점 규칙 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '상벌점 규칙의 이름',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'min_point',
            'description': '최소 점수',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
        {
            'name': 'max_point',
            'description': '최대 점수',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '상벌점 데이터 등록 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
