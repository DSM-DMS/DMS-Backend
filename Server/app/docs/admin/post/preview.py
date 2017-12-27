FAQ_PREVIEW_POST = {
    'tags': ['게시글 관리'],
    'description': 'FAQ 프리뷰 설정',
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
            'description': 'FAQ ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '프리뷰 설정 성공'
        },
        '204': {
            'description': '존재하지 않는 게시글'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

NOTICE_PREVIEW_POST = {
    'tags': ['게시글 관리'],
    'description': '공지사항 프리뷰 설정',
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
            'description': '공지사항 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '프리뷰 설정 성공'
        },
        '204': {
            'description': '존재하지 않는 게시글'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

RULE_PREVIEW_POST = {
    'tags': ['게시글 관리'],
    'description': '기숙사규정 프리뷰 설정',
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
            'description': '기숙사규정 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '프리뷰 설정 성공'
        },
        '204': {
            'description': '존재하지 않는 게시글'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
