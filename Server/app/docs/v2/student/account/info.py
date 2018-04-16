APPLY_INFO_GET = {
    'tags': ['계정'],
    'description': '신청 정보 조회',
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
            'description': '신청 정보 조회 성공',
            'examples': {
                'application/json': {
                    'extension_11': {
                        'class': 2,
                        'seat': 13
                    },
                    'extension_12': None,
                    'goingout': {
                        'sat': True,
                        'sun': False
                    },
                    'stay_value': 4
                }
            }
        },
        '403': {
            'description': '권한 없음(재로그인 필요)'
        }
    }
}

MYPAGE_GET = {
    'tags': ['계정'],
    'description': '마이페이지 정보 조회',
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
            'description': '마이페이지 조회 성공',
            'examples': {
                'application/json': {
                    'name': '조민규',
                    'number': 20120,
                    'goodPoint': 1,
                    'badPoint': 458756945
                }
            }
        },
        '403': {
            'description': '권한 없음(재로그인 필요)'
        }
    }
}

POINT_HISTORY_GET = {
    'tags': ['계정'],
    'description': '상벌점 기록 조회',
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
            'description': '내역 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'time': '2017-12-17',
                        'reason': '치킨 먹음',
                        'pointType': False,
                        'point': 3
                    },
                    {
                        'time': '2017-12-19',
                        'reason': '치킨 맛있음',
                        'pointType': True,
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
