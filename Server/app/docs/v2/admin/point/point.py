from app.docs.v2 import SAMPLE_OBJECT_IDS, jwt_header, json_parameter

POINT_GET = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '특정 학생의 상벌점 내역을 조회합니다.',
    'parameters': [
        jwt_header,
        json_parameter('id', '내역 조회 대상 학생 ID')
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
        jwt_header,
        json_parameter('id', '상벌점 데이터 등록 대상 학생 ID'),
        json_parameter('ruleId', '상벌점을 부여하기 위한 규칙 ID'),
        json_parameter('applyGoodPoint', '점수의 종류 (상점: true, 벌점 false)', type='bool'),
        json_parameter('point', '부여할 점수 (음수도 가능)', type='int')
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
        jwt_header,
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
