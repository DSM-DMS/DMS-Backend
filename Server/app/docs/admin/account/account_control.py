ACCOUNT_CONTROL_POST = {
    'tags': ['관리자 계정'],
    'description': '계정 삭제 후 새로운 UUID 생성',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'number',
            'description': '학번',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '계정 삭제, UUID 생성 성공',
            'examples': {
                'application/json': {
                    'UUID':  '022d'
                }
            }
        },
        '204': {
            'description': '해당 학번에 해당하는 계정, UUID 없음'
        },
        '401': {
            'description': 'JWT Token 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
