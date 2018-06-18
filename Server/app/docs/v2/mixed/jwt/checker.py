from app.docs.v2 import jwt_header

AUTH_CHECK_GET = {
    'tags': ['[Mixed] JWT 관련'],
    'description': '해당 Access Token이 유효한지(\'로그인되어 있음\'으로 표현할 수 있는지) 체크합니다.',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': 'Access Token이 유효함',
        },
        '204': {
            'description': 'Access Token이 유효하지 않음'
        }
    }
}
