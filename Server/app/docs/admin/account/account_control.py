ACCOUNT_CONTROL_DELETE = {
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
        '200': {
            'description': '계정 삭제 성공',
            },
        '204': {
            'description': '해당 학번에 해당하는 계정 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

ACCOUNT_CONTROL_GET = {
    'tags': ['관리자 계정'],
    'description': 'UUID 받아오기',
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
        '200': {
            'description': '성공',
            'examples': {
                'application/json': {
                    'UUID': '022d'
                }
            }
        },
        '204': {
            'description': '이미 가입된 학번'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
