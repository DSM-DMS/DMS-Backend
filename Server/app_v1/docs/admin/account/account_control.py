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

ACCOUNT_CONTROL_DELETE = {
    'tags': ['관리자 계정'],
    'description': '관리자 계정 삭제',
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
            'description': '삭제할 관리자 계정 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '계정 삭제, UUID 생성 성공'
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

STUDENT_SIGN_STATUS_GET = {
    'tags': ['관리자 계정'],
    'description': '학생 계정 회원가입 상태(카운트) 확인',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                'application/json': {
                    'unsigned_student_count': 103,
                    'signed_student_count': 124
                }
            }
        },
        '401': {
            'description': 'JWT Token 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
