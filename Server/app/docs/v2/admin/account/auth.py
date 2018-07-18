from app.docs.v2 import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN, json_parameter

AUTH_POST = {
    'tags': ['[Admin] 계정'],
    'description': '로그인',
    'parameters': [
        json_parameter('id', '로그인할 관리자 ID'),
        json_parameter('password', '로그인할 관리자 비밀번호')
    ],
    'responses': {
        '201': {
            'description': '로그인에 성공하여 Access Token과 Refresh Token을 반환합니다.',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}
