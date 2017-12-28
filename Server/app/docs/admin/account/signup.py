NEW_ACCOUNT_POST = {
    'tags': ['관리자 계정'],
    'description': '관리자 계정 생성',
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
            'description': '생성할 관리자 계정 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '생성할 관리자 계정 PW',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '생성활 관리자 계정 이름',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '계정 생성 성공'
        },
        '204': {
            'description': '계정 생성 실패(이미 존재하는 ID)'
        },
        '401': {
            'description': 'JWT Token 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
