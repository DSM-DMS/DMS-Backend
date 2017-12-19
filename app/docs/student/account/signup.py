ID_VERIFICATION_POST = {
    'tags': ['계정'],
    'description': 'ID 중복체크',
    'parameters': [
        {
            'name': 'id',
            'description': '중복 여부를 체크할 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'ID 중복되지 않음'
        },
        '204': {
            'description': 'ID 중복됨'
        }
    }
}

UUID_VERIFICATION_POST = {
    'tags': ['계정'],
    'description': 'UUID 유효성 검사',
    'parameters': [
        {
            'name': 'uuid',
            'description': '가입 가능 여부를 체크할 UUID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '가입 가능한 UUID'
        },
        '204': {
            'description': '가입 불가능한 UUID'
        }
    }
}
