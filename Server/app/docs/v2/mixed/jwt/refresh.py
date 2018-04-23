from app.docs.v2 import SAMPLE_ACCESS_TOKEN

REFRESH_GET = {
    'tags': ['[Mixed] JWT 관련'],
    'description': 'JWT Refresh Token을 이용해 Access Token을 새로 발급합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Refresh Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'Access Token 재발급에 문제 없으며, 새로운 Access Token을 반환합니다.',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN
                }
            }
        },
        '205': {
            'description': '해당 Refresh Token 발급 당시(로그인 시) 사용한 비밀번호가 변경되어, 재로그인 필요'
        },
        '401': {
            'description': 'Refresh Token이 만료됨'
        }
    }
}
