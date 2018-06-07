from app.docs.v2 import SAMPLE_OBJECT_IDS

POINT_GET = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '특정 학생의 상벌점 내역을 조회합니다.',
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
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '내역 조회 성공',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'date': '2017-12-17',
                        'reason': '치킨 먹음',
                        'pointType': False,
                        'point': 3
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'date': '2017-12-19',
                        'reason': '치킨 맛있음',
                        'pointType': False,
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

POINT_POST = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '특정 학생에 대해 상벌점을 부여합니다.',
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
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'ruleId',
            'description': '상벌점을 부여하기 위한 규칙 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'applyGoodPoint',
            'description': '점수를 상점에 부여할지, 벌점에 부여할지(상점인 경우 true, 벌점인 경우 false)',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'point',
            'description': '점수(증가일 경우 양수, 삭감일 경우 음수)',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '상벌점 부여에 성공하였으며, 해당 상벌점 부여에 대한 기록의 ID를 반환합니다.',
            'examples': {
                '': {
                    'id': SAMPLE_OBJECT_IDS[0]
                }
            }
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

POINT_DELETE = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '특정 학생의 상벌점 기록을 삭제합니다.',
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
            'description': '상벌점 데이터 삭제 대상 학생 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'historyId',
            'description': '삭제할 상벌점 기록 ID',
            'in': 'json',
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
            'description': '존재하지 않는 상벌점 기록 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
