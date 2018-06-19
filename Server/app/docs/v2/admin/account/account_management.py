from app.docs.v2 import SAMPLE_UUID, jwt_header

STUDENT_ACCOUNT_DELETE = {
    'tags': ['[Admin] 계정 관리'],
    'description': '학생 계정을 제거하고, 새로운 UUID를 생성해 반환합니다.',
    'parameters': [
        jwt_header,
        {
            'name': 'number',
            'description': '제거하고자 하는 학생의 학번',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '이미 제거되어 있었으며, 해당 학생에 대해 매핑되어 있던 기존의 UUID를 반환합니다.',
            'examples': {
                '': {
                    'uuid': SAMPLE_UUID
                }
            }
        },
        '201': {
            'description': '학생 계정이 제거되었으며, 새롭게 생성된 UUID를 반환합니다.',
            'examples': {
                '': {
                    'uuid': SAMPLE_UUID
                }
            }
        },
        '204': {
            'description': '존재하지 않는 학번'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

ADMIN_ACCOUNT_POST = {
    'tags': ['[Admin] 계정 관리'],
    'description': '새로운 관리자 계정을 생성합니다.',
    'parameters': [
        jwt_header,
        {
            'name': 'id',
            'description': '생성할 관리자 계정의 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'password',
            'description': '생성할 관리자 계정의 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'name',
            'description': '생성할 관리자 계정의 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '새로운 관리자 계정 생성 성공'
        },
        '409': {
            'description': '이미 존재하는 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

ADMIN_ACCOUNT_DELETE = {
    'tags': ['[Admin] 계정 관리'],
    'description': '만들어진 관리자 계정을 제거합니다.',
    'parameters': [
        jwt_header,
        {
            'name': 'id',
            'description': '제거할 관리자 계정의 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '관리자 계정 제거 성공'
        },
        '204': {
            'description': '존재하지 않는 괸리자 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
