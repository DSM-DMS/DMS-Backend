STAY_GET = {
    'tags': ['신청'],
    'description': '잔류신청 정보 조회',
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
            'description': '잔류신청 정보 조회 성공',
            'examples': {
                'application/json': {
                    'value': 4
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

STAY_POST = {
    'tags': ['신청'],
    'description': '잔류신청. 신청 시간은 일요일 오후 8시 30분부터 목요일 10시까지',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'value',
            'description': '''
            잔류신청 상태
            1: 금요귀가
            2: 토요귀가
            3: 토요귀사
            4: 잔류
            ''',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '잔류신청 성공'
        },
        '204': {
            'description': '잔류신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
