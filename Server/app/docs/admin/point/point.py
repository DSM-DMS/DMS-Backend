POINT_MANAGING_GET = {
    'tags': ['상벌점 관리'],
    'description': '특정 학생의 상벌점 내역 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '내역 조회 대상 학생 ID',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '내역 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'time': '2017-12-17',
                        'reason': '치킨 먹음',
                        'point': -3
                    },
                    {
                        'time': '2017-12-19',
                        'reason': '치킨 맛있음',
                        'point': 2
                    }
                ]
            }
        },
        '204': {
            'description': '존재하지 않는 학생 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POINT_MANAGING_POST = {
    'tags': ['상벌점 관리'],
    'description': '특정 학생에 대한 상벌점 부여',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '상벌점 데이터 등록 대상 학생 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'rule_id',
            'description': '상벌점을 부여하기 위한 규칙 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'point',
            'description': '상벌점(상점은 양수, 벌점은 음수)',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '상벌점 데이터 등록 성공'
        },
        '204': {
            'description': '존재하지 않는 학생 ID'
        },
        '205': {
            'description': '존재하지 않는 규칙 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POINT_MANAGING_DELETE = {
    'tags': ['상벌점 관리'],
    'description': '상벌점 데이터 삭제',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'student_id',
            'description': '상벌점 데이터 삭제 대상 학생 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'point_id',
            'description': '삭제할 상벌점 데이터 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '상벌점 데이터 삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 학생 ID'
        },
        '205': {
            'description': '존재하지 않는 상벌점 데이터 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}