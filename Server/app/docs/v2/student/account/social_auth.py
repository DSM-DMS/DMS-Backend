from app.docs.v2 import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN

ADD_SOCIAL_ACCOUNT_POST = {
    'tags': ['소셜 계정'],
    'description': '소셜 계정 연동',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'socialPlatform',
            'description': '소셜 계정 플랫폼',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'uuid',
            'description': '소셜 계정 구분자',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '소셜 계정 연동 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SOCIAL_AUTH_POST = {
    'tags': ['소셜 계정'],
    'description': '소셜 계정 로그인',
    'parameters': [
        {
            'name': 'uuid',
            'description': '소셜 계정 구분자',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '소셜 로그인 성공',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': '소셜 로그인 실패'
        }
    }
}
