VERSION_GET = {
    'tags': ['버전'],
    'description': '플랫폼의 최신 버전 조회',
    'parameters': [
        {
            'name': 'platform',
            'description': '최신 버전 조회할 플랫폼',
            'in': 'queryString',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '최신 버전 조회 성공'
        }
    }
}

VERSION_POST = {
    'tags': ['버전'],
    'description': '플랫폼의 최신 버전 등록',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'Admin JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'platform',
            'description': '최신 버전 등록할 플랫폼',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'version',
            'description': '최신 버전 등록할 플랫폼의 버전',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '최신버전 등록 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}