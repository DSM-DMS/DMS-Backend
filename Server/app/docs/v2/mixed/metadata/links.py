LINKS_GET = {
    'tags': ['[Mixed] 메타데이터'],
    'description': 'DMS에 관련된 링크 정보를 조회합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '정보 조회 성공',
            'examples': {
                '': {
                    'Facebook': 'https://www.facebook.com/DMSforDSM/',
                    'Github': 'https://github.com/DSM-DMS'
                }
            }
        }
    }
}
