STUDENT_MANAGING_GET = {
    'tags': ['상벌점 관리'],
    'description': '학생 목록 조회',
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
            'description': '목록 조회 성공. 상벌점 데이터가 없는 경우 상벌점과 벌점 교육 단계가 null입니다.',
            'examples': {
                'application/json': [
                    {
                        'id': 'city7310',
                        'name': '조민규',
                        'number': 2120,
                        'good_point': 1,
                        'bad_point': 50,
                        'penalty_training_status': 4
                    },
                    {
                        'id': 'geni429',
                        'name': '정근철',
                        'number': 2117,
                        'good_point': None,
                        'bad_point': None,
                        'penalty_training_status': None
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

STUDENT_MANAGING_POST = {
    'tags': ['상벌점 관리'],
    'description': '상벌점 데이터 등록',
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
            'name': 'good_point',
            'description': '상점',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
        {
            'name': 'bad_point',
            'description': '벌점',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
        {
            'name': 'penalty_training_status',
            'description': '벌점 교육 단계',
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
        '403': {
            'description': '권한 없음'
        }
    }
}

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
            'in': 'formData',
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
                        'time': '2017-12-17 14:22:18',
                        'reason': '치킨 먹음',
                        'point': -3
                    },
                    {
                        'time': '2017-12-19 16:10:45',
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
