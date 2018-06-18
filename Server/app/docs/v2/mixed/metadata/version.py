from app.docs.v2 import jwt_header

VERSION_GET = {
    'tags': ['[Mixed] 메타데이터'],
    'description': '해당 플랫폼의 최신 버전을 응답합니다.',
    'parameters': [
        {
            'name': 'platform',
            'description': '플랫폼 number(1: 웹, 2: 안드로이드, 3: iOS)',
            'in': 'path',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '해당 플랫폼의 최신 버전을 응답합니다.',
            'examples': {
                '': {
                    'version': '1.9'
                }
            }
        },
        '204': {
            'description': '해당 플랫폼에 대해 존재하는 버전 데이터가 없습니다.'
        }
    }
}

VERSION_PUT = {
    'tags': ['[Mixed] 메타데이터'],
    'description': '해당 플랫폼의 새로운 버전을 업로드합니다.',
    'parameters': [
        jwt_header,
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
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '버전 업로드 성공',
        }
    }
}
