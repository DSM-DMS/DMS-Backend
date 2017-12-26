FACILITY_REPORT_POST = {
    'tags': ['신고'],
    'description': '시설고장신고',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '시설고장신고 제목',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '시설고장신고 제목',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'room',
            'description': '호실 번호',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '시설고장신고 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
