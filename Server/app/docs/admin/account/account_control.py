ACCOUNT_DELETE = {
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
            'description': '학번에 해당하는 계정 없음'
        },
        '401': {
            'description': 'JWT Token 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

UUID_GET = {
    'tags': ['계정'],
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
                    'UUID': '022db29c-d0e2-11e5-bb4c-60f81dca7676'
                }
            }
        },
        '204': {
            'description': '이미 가입된 학번'
        },
        '401': {
            'description': 'JWT Token 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}