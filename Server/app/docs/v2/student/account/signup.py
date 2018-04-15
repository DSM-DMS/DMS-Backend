ID_VERIFICATION_POST = {
    'tags': ['계정'],
    'description': 'ID 중복체크',
    'parameters': [
        {
            'name': 'id',
            'description': '중복 여부를 체크할 ID',
            'in': 'json',
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
            'in': 'json',
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

SIGNUP_POST = {
    'tags': ['계정'],
    'description': '회원가입',
    'parameters': [
        {
            'name': 'uuid',
            'description': 'UUID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '사용자 PW',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '가입 완료'
        },
        '204': {
            'description': '가입 불가능(이미 가입된 ID)'
        },
        '205': {
            'description': '가입 불가능(유효하지 않은 UUID)'
        }
    }
}
