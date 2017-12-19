MYPAGE_GET = MYPAGE_GET = {
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
                    'signup_date': '2017-10-10',
                    'name': '조민규',
                    'number': 20120,
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
            'description': '해당 학생 정보 없음(재로그인 필요)'
        }
    }
}
