BUG_REPORT_POST = {
    'tags': ['신고'],
    'description': '버그 신고',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'platform',
            'description': '버그 신고를 한 플랫폼',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '버그 신고 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '버그 신고 성공'
        },
        '400': {
            'description': 'platform이나 content가 빈칸'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
