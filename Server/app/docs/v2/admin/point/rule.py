from app.docs.v2 import SAMPLE_OBJECT_IDS

RULE_GET = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '상벌점 규칙 목록을 조회합니다.',
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
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'name': '치킨이 맛있는 규칙',
                        'pointType': True,
                        'minPoint': 1,
                        'maxPoint': 3
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'name': '저녁에 배고픈 규칙',
                        'pointType': False,
                        'minPoint': 1,
                        'maxPoint': 3
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

RULE_POST = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '상벌점 규칙을 추가합니다.',
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
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pointType',
            'description': 'true: 상점, false: 벌점',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'minPoint',
            'description': '최소 점수',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'maxPoint',
            'description': '최대 점수',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '상벌점 규칙 등록에 성공했으며, 등록된 규칙의 ID를 응답합니다.',
            'examples': {
                '': {
                    'id': SAMPLE_OBJECT_IDS[0]
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

RULE_ALTERATION_PATCH = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '상벌점 규칙의 내용을 수정합니다.',
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
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '상벌점 규칙의 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pointType',
            'descriptions': 'true: 상점, false: 벌점',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'minPoint',
            'description': '최소 점수',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'maxPoint',
            'description': '최대 점수',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '상벌점 규칙 수정 성공'
        },
        '204': {
            'description': '존재하지 않는 규칙 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

RULE_ALTERATION_DELETE = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '상벌점 규칙을 삭제합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'ruleId',
            'description': '삭제할 상벌점 규칙 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '상벌점 규칙 삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 규칙 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
