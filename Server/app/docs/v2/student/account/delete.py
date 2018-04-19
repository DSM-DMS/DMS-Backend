DELETE_ACCOUNT_DELETE = {
    'tags': ['계정'],
    'description': '학생 자신의 계정을 삭제합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '현재 아이디',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'password',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '계정 삭제 성공'
        },
        '403': {
            'description': '비밀번호 변경 실패(틀린 ID나 비밀번호), 또는 권한 없음'
        }
    }
}
