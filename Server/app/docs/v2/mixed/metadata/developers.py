DEVELOPER_INFO_GET = {
    'tags': ['메타데이터'],
    'description': 'DMS 개발자 정보를 조회합니다.',
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
                    'App': [
                        '조성빈',
                        '이병찬',
                        '윤정현',
                        '이성현'
                    ],
                    'Backend': [
                        '김성래',
                        '조민규',
                        '인상민'
                    ]
                }
            }
        }
    }
}
