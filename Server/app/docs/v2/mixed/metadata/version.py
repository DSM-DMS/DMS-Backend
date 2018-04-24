VERSION_GET = {
    'tags': ['[Mixed] 메타데이터'],
    'description': '해당 플랫폼의 버전이 최신인지 조회합니다.',
    'parameters': [
        {
            'name': 'platform',
            'description': '플랫폼 number(1: 웹, 2: 안드로이드, 3: iOS)',
            'in': 'query',
            'type': 'str',
            'required': True
        },
        {
            'name': 'version',
            'description': '해당 클라이언트의 버전',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '최신 버전임',
        },
        '204': {
            'description': '최신 버전이 아니며, 해당 플랫폼의 최신 버전을 응답합니다.',
            'examples': {
                '': {
                    'version': '1.9'
                }
            }
        }
    }
}

VERSION_POST = {
    'tags': ['[Mixed] 메타데이터'],
    'description': '해당 플랫폼의 새로운 버전을 업로드합니다.',
    'parameters': [
        {
            'name': 'platform',
            'description': '플랫폼 number(1: 웹, 2: 안드로이드, 3: iOS)',
            'in': 'query',
            'type': 'str',
            'required': True
        },
        {
            'name': 'version',
            'description': '새로운 버전',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '버전 업로드 성공',
        }
    }
}
