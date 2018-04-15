DELETE_ACCOUNT_DELETE = {
    'tags': ['계정'],
    'description': '계정 삭제',
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
            'name': 'pw',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '계정 삭제 성공'
        },
        '403': {
            'description': '비밀번호 변경 실패(틀린 id or 틀린 pw) or 권한 없음'
        }
    }
}
