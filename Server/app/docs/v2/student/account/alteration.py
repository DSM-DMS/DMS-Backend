from app.docs.v2 import jwt_header

CHANGE_PW_POST = {
    'tags': ['[Student] 계정 관리'],
    'description': '비밀번호를 변경합니다.',
    'parameters': [
        jwt_header,
        {
            'name': 'currentPassword',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'newPassword',
            'description': '바꿀 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '비밀번호 변경 성공'
        },
        '403': {
            'description': '비밀번호 변경 실패(틀린 비밀번호), 또는 권한 없음'
        },
        '409': {
            'description': '현재 비밀번호와 새 비밀번호가 동일함'
        }
    }
}
